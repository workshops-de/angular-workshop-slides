---
name: task-creator
description: Writes & checks workshop lessons based on given templates
---

# SKILL.md

A lesson consists of a `body.md`, `hint.md` and an optional `bonus.md`.

## Structure of a lesson

```
lessons/
- 01-my-lesson/
   - task.yml
   - body.md
   - hint.md
   - bonus.md # optional
   - assets/ # optional - images linked in md-files of the task
```

## Task metadata

- A task has a `task.yml` file with technical details to include the task in the eClassroom
- Use [task.template.md](./references/task.template.yml) if you need to write/update one.
- A solution-Commit has the structure: solution--<topic>-<topic-part>
  - derive the title of a task from <topic-parts>

## Write understandable tasks

- The task description shall guide the attendee to solve a task alone.
- Although we want to provide all details needed to solve a task we do not overwhelm the attendee with a wall of text. Include what is really needed.
- Follow the [body template](./references/body.template.md) to learn about the structure
  - Each task is separated by `---` to make the overall text more readable

## Inline code highlighting

The eClassroom Markdown parser highlights code with [Shiki](https://shiki.style/packages/rehype#inline-code) (`inline: 'tailing-curly-colon'`).
Inline code is highlighted by appending a `{:<lang>}` marker **inside** the backticks, directly after the code:

| Write this                 | Instead of this   | Language |
| -------------------------- | ----------------- | -------- |
| `` `input(){:ts}` ``       | `` `input()` ``   | `ts`     |
| `` `[content]{:html}` ``   | `` `[content]` `` | `html`   |
| `` `<input>{:html}` ``     | `_<input>_`       | `html`   |
| `` `count = signal(0){:ts}` `` | `` `count = signal(0)` `` | `ts` |

Rules:

- Applies to `body.md`, `hint.md` and `bonus.md`.
- The marker sits inside the backticks: `` `code{:ts}` `` ✅, `` `code`{:ts} `` ❌.
- Always use a marker for code (TypeScript → `ts`, templates → `html`, styles → `css`, shell → `bash`); a code span without marker stays unhighlighted.
- Use it for code snippets, identifiers, bindings and API calls. Plain terms, file names and paths (`src/app/app.ts`) and UI labels stay without a marker or in _italics_ as before.
- When updating an existing lesson, add the marker to the inline code you touch; do not rewrite untouched lessons.
- Code blocks keep using fenced blocks with a language (` ```ts `, ` ```html `) as shown in the [hint template](./references/hint.template.md).

## Provide valuable hints

- Hints...
  - contain technical details on how the task has to be solved.
  - Attendees are considered to learn a complete new area.
  - are an important pillar to provide code snippets, to help with syntax and understanding
  - should follow the order of task steps defined in the corresponding `body.md`.
  - are a safe harbour for an attendee. Easy to follow, no tricks. Straight forward code hints to get the solution work.

## Bonus

- If you write a new task, ask if you should add a bonus.
- Bonus descriptions are for fast and more experienced attendees.
- Recommend a bonus task that fits the respective topic
- Bonus tasks also follow the [body template](./references/body.template.md)
