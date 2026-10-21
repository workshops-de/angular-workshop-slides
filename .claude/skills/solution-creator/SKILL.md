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

## Solution commit messages

The commit message of a solution commit **is** the tag name (`tools/recreate-tags.sh` creates one tag per commit),
and the tag name is referenced by `git_tag_completed` in the lesson's `task.yml`. A wrong message therefore breaks the
"What's changed" diff in the eClassroom.

- Format: `solution--<topic>[-<part>...]`, e.g. `solution--service`, `solution--router-guards-canMatch`
  - starts with `solution--` (two dashes)
  - segments separated by a single `-`, only letters and digits, camelCase allowed
  - the first segment starts with a lowercase letter
  - only the first line counts as tag name, keep anything else (e.g. trailers) below an empty line
- The message must match `git_tag_completed` of the corresponding `task.yml` exactly.
- Renaming a solution commit means renaming the tag: update the `task.yml` in the same change.

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

- Run `ng build` at every changed solution commit and at the tip of the solution branch.
- A rebase rewrites the history of the already published solution branch. Publishing it needs a force push and new tags.
  Never do this without the trainer's explicit approval:

```bash
git push --force-with-lease origin solution
tools/recreate-tags.sh --dry-run   # validates commit messages, lists moved, new and stale tags
tools/recreate-tags.sh --prune     # recreates and pushes all tags, deletes stale remote tags
```

- Finally, switch back to the base branch after your work is done

```bash
git checkout main
```
