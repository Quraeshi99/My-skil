# Engineering Governance: The Karpathy Standard

This project implements the behavioral guidelines derived from Andrej Karpathy's observations on LLM coding pitfalls.

## 1. Think Before Coding
- **Assume Nothing:** Explicitly state all assumptions before the first line of code.
- **Surface Ambiguity:** If a request can be interpreted in multiple ways, present options instead of picking one silently.
- **Push Back:** If the requested approach is overcomplicated or inefficient, suggest a simpler alternative.

## 2. Simplicity First
- **Minimum Viable Code:** Implement the smallest amount of code that solves the problem.
- **No Speculative Engineering:** Do not add "flexibility" or "configurability" unless explicitly requested.
- **The Senior Engineer Test:** If a senior engineer would find the abstraction bloated, it must be simplified.

## 3. Surgical Changes
- **Zero Side-Effects:** Changes must be orthogonal to unrelated code.
- **Style Matching:** Follow the existing codebase style, regardless of personal preference.
- **Orphan Cleanup:** Remove only the imports/variables made unused by the current change.

## 4. Goal-Driven Execution
- **Declarative Goals:** Shift from "Do X" $ightarrow$ "Verify Y".
- **Test-First Loop:**
  1. Write a test that reproduces the bug or defines the feature.
  2. Implement the fix/feature.
  3. Verify the test passes.
- **Execution Plan:** For multi-step tasks, provide a brief `Step` $ightarrow$ `Verify` plan.
