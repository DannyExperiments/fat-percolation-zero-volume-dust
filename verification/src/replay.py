"""Finite exact checks for the block-cube geometry and probability recurrence."""

from fractions import Fraction
from itertools import combinations, product
from math import comb


def grid(side, dimension):
    return tuple(product(range(side), repeat=dimension))


def neighbors(vertex, side):
    for axis, coordinate in enumerate(vertex):
        for step in (-1, 1):
            if 0 <= coordinate + step < side:
                yield vertex[:axis] + (coordinate + step,) + vertex[axis + 1:]


def connected(vertices, side):
    remaining = vertices.copy()
    queue = [remaining.pop()]
    for current in queue:
        for vertex in neighbors(current, side):
            if vertex in remaining:
                remaining.remove(vertex)
                queue.append(vertex)
    return not remaining


def aligned_pairs(side, dimension, axis):
    return [
        (position, position[:axis] + (0,) + position[axis + 1:])
        for position in grid(side, dimension) if position[axis] == side - 1
    ]


def check_geometry():
    grids = 0
    contacts = 0
    for side, dimension in ((4, 2), (9, 2), (4, 3), (4, 4)):
        vertices = set(grid(side, dimension))
        for hole in (None, *sorted(vertices)):
            retained = vertices - {hole}
            assert connected(retained, side)
            for axis in range(dimension):
                assert any(vertex[axis] == 0 for vertex in retained)
                assert any(vertex[axis] == side - 1 for vertex in retained)
            grids += 1
        for axis in range(dimension):
            pairs = aligned_pairs(side, dimension, axis)
            # An off-face deletion has the same effect on alignment as deleting nothing.
            left = [None, *(a for a, _ in pairs)]
            right = [None, *(b for _, b in pairs)]
            for a, b in product(left, right):
                assert sum(c != a and d != b for c, d in pairs) >= side**(dimension - 1) - 2
                contacts += 1
    pairs = aligned_pairs(4, 2, 0)
    histogram = {2: 0, 3: 0, 4: 0}
    for left, right in product((None, *grid(4, 2)), repeat=2):
        intact = sum(a != left and b != right for a, b in pairs)
        histogram[intact] += 1
    assert histogram == {2: 12, 3: 108, 4: 169}
    assert all(a == (1, 0) or b == (0, 1) for a, b in aligned_pairs(2, 2, 0))
    return grids, contacts, histogram


def local_pass(j):
    def retain(n):
        return 1 - Fraction(1, (n + 1)**2)
    return retain(2*j) * retain(2*j + 1)**4


def defect(j, horizon):
    children = 16
    failed = 1 - local_pass(horizon)
    for level in range(horizon - 1, j - 1, -1):
        survive = 1 - failed
        failed = 1 - local_pass(level) * (survive**children + children * failed * survive**(children - 1))
    return failed


def check_probabilities():
    child_count = 16
    pair_count = comb(child_count, 2)
    delta = Fraction(1, 2 * pair_count)
    checks = 0
    for start in (30, 40, 60):
        previous = Fraction(0)
        for horizon in range(start, start + 3):
            bound = sum((Fraction(1, (2*h + 1)**2) + Fraction(4, (2*h + 2)**2)) / 2**(h-start)
                        for h in range(start, horizon + 1))
            failure = defect(start, horizon)
            assert previous < failure <= min(delta, bound)
            previous = failure
            checks += 1
        assert Fraction(1, (2*start + 1)**2) + Fraction(4, (2*start + 2)**2) < delta/2
    # For arbitrary nonnegative defects the finite geometric multiplicities are <2.
    assert all(sum(Fraction(1, 2**i) for i in range(j + 1)) == 2 - Fraction(1, 2**j)
               for j in range(1, 65))
    return checks


def main():
    grids, contacts, histogram = check_geometry()
    print(f"Grid connectivity with zero or one missing child: {grids} cases")
    print(f"Face alignments with zero or one excluded pair per side: {contacts} cases")
    print(f"All 289 explorer selections, counts by surviving pair number: {histogram}")
    print(f"Exact finite-horizon probability checks: {check_probabilities()} (plus 64 geometric sums)")
    print("Finite replay passed. The infinite-depth and almost-everywhere claims use the written proof.")


if __name__ == "__main__":
    main()
