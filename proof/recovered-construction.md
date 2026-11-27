# Q1294: The dust in fat fractal percolation has zero volume

## Exact source

Broman, van de Brug, Camia, Joosten and Meester, *Fat fractal percolation and k-fractal percolation*, ALEA 9(2), 279–301 (2012), §1.2, Open Problem 1.10, [printed p. 283, PDF p. 5](https://alea.math.cnrs.fr/articles/v9/09-12.pdf#page=5):

> However, we do not have an example for which (1.3) holds, and we do not know whether (1.3) is possible at all.

Equation (1.3) on printed p. 282 is the alternative in which the dust has positive Lebesgue measure but the union of non-singleton components has measure zero almost surely on nonextinction. Kolossváry and Troscheit restate the same question as [Question 7.3](https://arxiv.org/html/2508.08150v1#S7) of their survey (arXiv:2508.08150v1, §7.1).

## Result

The answer is **no**. Fix integers \(N,d\ge2\). In the independent \(N\)-adic retention model on the closed unit cube, let the probability at level \(n\) be \(p_n\in(0,1]\), with \(\prod_n p_n>0\). Almost surely the set of points of the limiting compact set \(F\) whose connected component is a singleton has Lebesgue measure zero. The proof does not require monotonicity of the probabilities.

## 1. A probability bound for good cubes

Assign independent Bernoulli marks to *every* cube at every level, whether or not its ancestors are marked. The parameter of a mark at level \(n\) is \(p_n\). A cube is retained in the original construction exactly when its mark and all ancestral marks are one. Work with the labeled cubes of this tree, so that cubes touching along faces still have independent marks. Set \(q_n=1-p_n\). Then \(\sum_n q_n<\infty\) by \(-\log p_n\ge q_n\).

Use positive even levels \(2j\), \(j\ge1\), as block levels. The block children of a cube are its grandchildren, arranged in an \(L^d\) grid with \(L=N^2\ge4\). The local test at a level \(2j\) cube requires its own mark and the marks of all \(N^d\) immediate children to be one. Its failure probability is at most
\[
 r_j=q_{2j}+N^d q_{2j+1}.
\]
Here \(\sum_j r_j<\infty\), and \(r_j\to0\).

For a finite terminal block level \(m\), call a cube at level \(2m\) good if it passes its local test. Recursively, a level \(2j\) cube for \(j<m\) is good if it passes its local test and at most one block child is not good. These finite-horizon events decrease as \(m\) increases. Call a cube good without qualification if it passes at all finite horizons. Every good cube has at most one bad block child: if two children fail at any horizons, both fail at a common larger horizon, at which the parent cannot pass its recursive test.

Let \(b_j^{(m)}\) be the bad probability at block level \(j\) and horizon \(m\). The block-child events depend on disjoint families of marks and are independent. With \(C=\binom{L^d}{2}\), the union bound on pairs gives
\[
 b_m^{(m)}\le r_m,\qquad b_j^{(m)}\le r_j+C(b_{j+1}^{(m)})^2.
\]
Choose \(\delta=1/(2C)\) and \(J\) so that \(r_j\le\delta/2\) for all \(j\ge J\). Backward induction gives \(b_j^{(m)}\le\delta\) in this tail, since \(C\delta^2=\delta/2\). Hence the quadratic term is at most \(b_{j+1}^{(m)}/2\); iteration and passage to the increasing bad-event limit yield
\[
 b_j\le\sum_{h=j}^\infty 2^{-(h-j)}r_h,\qquad
 \sum_{j\ge J}b_j\le2\sum_{j\ge J}r_j<\infty. \tag{1}
\]

## 2. Why the good descendants genuinely form a continuum

For a good cube \(Q\), define \(K_0(Q)=Q\) and let \(K_h(Q)\) be the union of closed block descendants at distance \(h\) connected to \(Q\) by an entirely good chain of block cubes. These are nonempty nested compact sets. For each finite \(h\) establish both claims together:

1. \(K_h(Q)\) is connected for every good \(Q\).
2. If two good same-level cubes share a full face, their \(K_h\) sets intersect.

At \(h=0\) both are immediate. For claim 2 at \(h+1\), there are \(L^{d-1}\ge4\) aligned pairs of block children abutting the shared face. Each side can exclude at most one pair, so choose an aligned pair of good children. Their \(K_h\) sets intersect by claim 2 at depth \(h\); these sets are contained in the respective \(K_{h+1}\) sets. For claim 1 at \(h+1\), the good block children form a face-connected grid, since deleting at most one vertex from the \(d\)-dimensional nearest-neighbor grid with side length \(L\) does not disconnect it. To see this, take a first-coordinate slice different from the first coordinate of the removed vertex. Each remaining grid vertex can move in the first direction to the slice; if the missing vertex blocks that column, step once in a second coordinate within the grid, then move to the slice. The slice is connected and does not contain the removed vertex. Now the \(K_h\) sets of the good children are connected and intersect across their adjacency edges by the induction hypotheses, so their union is connected.

Thus \(K(Q)=\bigcap_{h\ge0}K_h(Q)\) is compact, nonempty and connected by nested compactness. It is not a singleton: each of the two opposite outer slabs of block children in the first coordinate has a good child, whose own nonempty limit set is contained in \(K(Q)\). The slabs are separated by distance \((1-2/L)\operatorname{side}(Q)>0\). Finally, if the original ancestors of \(Q\) are marked, \(K(Q)\subset F\): along each good chain, the local tests certify the even-level cubes and the intervening odd-level cubes; hence every \(K_h(Q)\) lies in the original level \(2j+2h\) retained union. This does not assume that arbitrary crossings inside adjacent cells glue.

## 3. Almost every point of the original set is covered

Outside the countable union of grid boundaries, each point \(x\) has a unique cube \(Q_j(x)\) at each block level. At level \(j\), the union of all bad block cubes has expected volume \(b_j\), because their interiors partition the unit cube and each cube has the same bad probability. By (1) and Tonelli, almost surely the sum of the volumes of these bad unions over \(j\ge J\) is finite. The measure-theoretic first Borel–Cantelli lemma now gives that for Lebesgue-almost every \(x\), all sufficiently deep \(Q_j(x)\) are good. This step does not assert independence along the chain of a point.

For such an \(x\in F\), take \(j\) after the last bad ancestor. Since \(x\) avoids boundaries and belongs to \(F\), all its original ancestors are marked. Its entire block chain at and below \(Q_j(x)\) is good, so \(x\in K(Q_j(x))\subset F\). This continuum has positive diameter. In particular \(x\) is not dust. The exceptional set has Lebesgue measure zero almost surely, as claimed. Under the monotone hypotheses of the source, its Theorem 1.7 also gives positive volume of \(F\) on nonextinction.

See the [updated literature comparison](../audits/public_safe_reports/LITERATURE.md) for the prior nearly full subtree construction and the precise printed exponent in Theorem 1.9(ii).
