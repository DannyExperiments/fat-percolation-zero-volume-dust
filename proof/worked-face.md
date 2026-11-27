# Two aligned pairs survive

Set N=2 and d=2. A block square's grandchildren form a 4×4 grid. Consider two horizontally adjacent good block squares. Their shared side has four aligned pairs, one per row. Delete the left square's seam tile in row 1 and the right square's seam tile in row 2.

```text
left block        right block
· · · ×      │    · · · ·   row 1, excluded on left
· · · ·      │    × · · ·   row 2, excluded on right
· · · ●──────┼────● · · ·   row 3, intact pair
· · · ●──────┼────● · · ·   row 4, intact pair
```

Here × marks a missing child and ● marks the two endpoints of a surviving aligned pair. If both deletions were on the same seam row, three pairs would survive. If neither were on the seam, all four would survive. Each square remains connected by face adjacencies after deleting its one child.

For the induction in the paper, take either surviving pair. Subdivide both of its squares again. The same count gives an aligned pair at the next block depth. The closed descendant unions have points in common across the original face at every finite depth. Their nested compact intersections therefore also meet. The finite figures show the alignment rule, while the full proof establishes the recursive and almost-everywhere conclusions.

[Offline explorer](../visualization/shared-face-explorer.zip) · [Written proof](../paper/manuscript.pdf) · [Exact replay](../verification/src/replay.py).
