# Agent Instructions
These rules are absolute. Every agent working on this project MUST follow them.

## THE ABSOLUTE FIRST RULE: Brain Setup
Before writing a single line of code or making any change, you MUST perform the 'White-Labeling Brain Setup'.
1. **Deep Analysis:** Analyze the entire project structure, data flow, and existing implementation.
2. **Memory Initialization:** If not already present, create and update the `ai/` directory:
   - `ai/current-state.md`: Factual snapshot of the project.
   - `ai/decisions.md`: Chronological record of technical decisions.
   - `ai/known-issues.md`: List of bugs and technical debt.
   - `ai/instructions.md`: This file.
3. **Context Sync:** You are not authorized to proceed until you have verified that the `ai/` memory is current.

## Core Behavioral Rules
- **No Blind Refactors:** Do not modify, rename, or delete existing source code without explicit user approval.
- **Verification Required:** Every task must end with proven output (Test logs, Lint results, Typecheck).
- **Decision Logging:** Every major technical change must be recorded in `ai/decisions.md`.

## Coding Standards
- Follow the 'Surgical Changes' principle.
- Prioritize simplicity over over-engineering.
- Ensure all tenant-scoped queries include `organization_id`.
