# Uniform budget for block defects

For an arbitrary finite horizon read backwards from the terminal cube, the quadratic pair-defect recursion keeps every failure bound below its small threshold and bounds the total by twice the sum of local errors. The certificate retains the final boundary term.

Independence gives the probability recursion. Passage to the infinite tail, face-connected descendants and the measure-zero conclusion are in the manuscript.

[Lean proof](Certificate.lean) · [Paper](../../paper/manuscript.pdf)

Run `python3 formal/closing/verify.py` from the repository root with the pinned Lean toolchain and mathlib dependencies available. The workflow sets up those versions, compiles the proof, and checks the names and axioms of the public declarations printed by the file.
