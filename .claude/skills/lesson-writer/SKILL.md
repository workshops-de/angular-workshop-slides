---
name: lesson-writer
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

## Write understandable tasks

- The task description shall guide the attendee to solve a task alone.
- Although we want to provide all details needed to solve a task we do not overwhelm the attendee with a wall of text. Include what is really needed.
- Follow the [body template](./references/body.template.md) to learn about the structure
  - Each task is separated by `---` to make the overall text more readable

## Provide valuable hints

- Hints contain technical details on how the task has to be solved.
- Attendees are considered to learn a complete new area.
- Hints are an important pillar to provide code snippets, to help with syntax and understanding
- Hints should follow the order of task steps defined in the corresponding `body.md`.

## Bonus

- If you write a new task, ask if you should add a bonus.
- Bonus descriptions are for fast and more experienced attendees.
- Recommend a bonus task that fits the respective topic
- Bonus tasks also follow the [body template](./references/body.template.md)
