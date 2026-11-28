import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
namespace BadBlock
open Finset
/-- Reverse the finite terminal levels, so level zero is the terminal cube.
The nonlinear pair-defect recursion gives a bound on the whole budget that
is uniform in the horizon. -/
theorem finite_budget (N : ℕ) (b r : ℕ → ℝ) (C δ : ℝ) (hc : 0 ≤ C)
    (hscale : C*δ = 1/2) (hr : ∀ i ≤ N, r i ≤ δ/2)
    (hn : ∀ i ≤ N, 0 ≤ b i) (h0 : b 0 ≤ r 0)
    (rec : ∀ i < N, b (i+1) ≤ r (i+1) + C*(b i)^2) :
    ∀ n ≤ N, b n ≤ δ ∧ (∑ i ∈ range (n+1), b i) + b n ≤ 2*∑ i ∈ range (n+1), r i := by
  have δ0 : 0 ≤ δ := by linarith [hr 0 (Nat.zero_le N),hn 0 (Nat.zero_le N)]
  intro n
  induction n with
  | zero => intro _; simp; constructor <;> linarith [hr 0 (Nat.zero_le N)]
  | succ n ind =>
    intro hN
    have hnN : n ≤ N := by omega
    have ih := ind hnN
    have step := mul_le_mul_of_nonneg_left ih.1 hc
    rw [hscale] at step
    have compare := mul_le_mul_of_nonneg_right step (hn n hnN)
    have linear : b (n+1) ≤ r (n+1) + b n/2 := by nlinarith [rec n (by omega)]
    constructor
    · linarith [hr (n+1) hN,ih.1]
    · rw [sum_range_succ,sum_range_succ (fun i => r i)]
      linarith [ih.2]
end BadBlock
#print axioms BadBlock.finite_budget
