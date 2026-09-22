---
name: solution-creator
description: Plans and applies solutions to workshop tasks. Automates the integration with git rebase
---

# SKILL.md

## Configuration

|                 | Value        | Description                                                                                                                                                                 |
| --------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| solution prefix | `solution--` | commit message prefix of a commit that contains a solution for a task                                                                                                       |
| solution branch | `solution`   | the branch where all task solutions live                                                                                                                                    |
| base branch     | `main`       | The branch where containing the starting point for attendees of the workshop                                                                                                |
| mode            | `submodule`  | Can be either `repository` or `submodule`. `repository`: find the branch in the root git repository. `submodule`: the repository contains a git submodule with the solution |

## Locating the commit

- If mode `submodule` is set via [Configuration](#configuration) locate the submodule by reading `.gitmodules`
  - if more than one submodule is defined aks which you should use
  - if no `gitmodules` is present, stop and ask for clarification
- List all solution--Commits (all commits starting with the solution prefix) to help the trainer to choose the correct spot
  - `git log --oneline solution-next 2>/dev/null | grep "solution--" || git log --oneline --all | grep "solution--"`
- Target commit
  - You need to know what commit should be updated
  - the commit must start with the solution-prefix
- If no valid commit is presented
  - Ask if a new solution-commit should be created
  - If yes ask where the commit needs to be created (between which commits in the solution branch)

## Defining the Scope

- Ask for the learning outcome for the workshop attendees
- Ask for the scope of the solution
- Aks where the solution should be placed

## Implement the solution

- Consult `/angular-developer`-Skill for best practices before you start coding
- Plan the solution and the code you want to write
- Present it and wait for approval before you apply it

### Integrate the solution

- After approval, write the code
- Apply it by rebasing the solution branch on the base branch
- Resolve occurring merge conflicts
  - If merge conflicts occur explain in detail how you resolve the conflicts and tell the reason behind the conflict

```bash
git checkout solution
git rebase main --interactive
# apply the new or updated solution
```

- Finally, switch back to the base branch after your work is done

```bash
git checkout main
```
