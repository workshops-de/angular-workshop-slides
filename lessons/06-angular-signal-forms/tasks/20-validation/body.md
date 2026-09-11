Let's add some Form Validation!

Signal Forms define validation next to the model, via a **schema function** — the second argument to `form()`. Inside it you get a `schemaPath` that mirrors your model's shape, and you attach validators like `required()` to individual paths (e.g. `schemaPath.isbn`).

- **Add a schema function** Pass a second argument to `form()`: a function `schemaPath => { ... }`.
- **Add validators** Inside that function call `required(schemaPath.isbn, { message: '...' })` for `isbn`, `title` and `author`. Import `required` from `@angular/forms/signals`.
- **Show validation errors** Now we can add some template logic whenever a field is in an error state:
  - Add a `@for`-Block with a `<small>`-Tag beneath the `<input>`-Tags of the `title` and `author`-Input, iterating over `form.title().errors()` (or `form.author().errors()`).
  - Only show the errors once the field was `touched()`, e.g. wrap the `@for` in `@if (form.title().touched()) { ... }`.
  - Print the error's `message` property inside the `<small>`-Tag.

> The Submit-Button is already disabled as long as the whole `form` is not in a valid state via `[disabled]="form().invalid()"` from the previous task.
