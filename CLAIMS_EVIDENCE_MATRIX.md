# Claims and evidence

| Claim | Evidence | Scope |
|---|---|---|
| Summable bad-cube probabilities | [Paper §2](paper/manuscript.pdf) | Independent labeled marks with positive retention product |
| Good block descendants form a nontrivial continuum | [Paper §3](paper/manuscript.pdf) · [Worked face](proof/worked-face.md) | Closed cubes; block grid side at least four |
| Singleton-component volume is zero | [Paper §4](paper/manuscript.pdf) | Almost sure Lebesgue measure statement |
| Relation to earlier block-tree and crossing approaches | [Literature comparison](audits/public_safe_reports/LITERATURE.md) | Dated search and explicit method attribution |
| Finite checks | [Exact replay](verification/results/replay.txt) | Geometry, all 289 explorer inputs and finite-horizon probabilities |

**Partial formalization.** For an arbitrary finite horizon read backwards from the terminal cube, the quadratic pair-defect recursion keeps every failure bound below its small threshold and bounds the total by twice the sum of local errors. The certificate retains the final boundary term. Independence gives the probability recursion. Passage to the infinite tail, face-connected descendants and the measure-zero conclusion are in the manuscript. [Lean source](formal/closing/Certificate.lean)
