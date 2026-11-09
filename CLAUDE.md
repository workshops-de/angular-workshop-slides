# Lessons

This repository only contains lessons for the Angular Workshop.
To understand how to structure lessons and tasks, in order to create and update them correctly, use the
`course-content` skill from the workshops.de `workshops-courses` Claude Code plugin (enabled in
`.claude/settings.json`, source: [workshops-de/claude-plugins](https://github.com/workshops-de/claude-plugins)).
This repository uses two-digit task folders stepped by 10 (`10-service`, `20-http`, …) and
`git_tag_completed: solution--<task-slug>`.

# Slides

Currently, no slidev slides are planned in this repository.
Slides live at Google Slides.
Topics are spread among different presentations.

Use `./.claude/skills/google-slides-workshop-teacher` to learn how slides are updated.

# Commit Conventions

This repo enforces [Conventional Commits](https://www.conventionalcommits.org/) via a Husky `commit-msg` hook
(commitlint) plus a GitHub Actions backstop. Run `npm install` once to activate the local hook. Details and
examples: [commit-conventions.md](./docs/commit-conventions.md).

# Sample Solutions

The `sample-solution` directory (in the `angular-workshop` repository, added there as a git submodule pointing to `git@github.com:workshops-de/angular-workshop.git`) contains the sample solutions for the lessons' tasks. Each commit in that submodule is the solution to one task.
