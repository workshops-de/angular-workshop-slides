Let's add some Form Validation!

Signal Forms define validation next to the model, via a **schema function** — the second argument to `form(){:ts}`. Inside it you get a `schemaPath{:ts}` that mirrors your model's shape, and you attach validators like `required(){:ts}` to individual paths (e.g. `schemaPath.isbn{:ts}`).

- **Add a schema function** Pass a second argument to `form(){:ts}`: a function `schemaPath => { ... }{:ts}`.

---

- **Add validators** Inside that function call `required(schemaPath.isbn, { message: '...' }){:ts}` for `isbn{:ts}`, `title{:ts}` and `author{:ts}`. Import `required{:ts}` from `@angular/forms/signals`.

---

- **Show validation errors** Now we can add some template logic whenever a field is in an error state:
  - Add a `@for{:html}`-Block with a `<small>{:html}`-Tag beneath the `<input>{:html}`-Tags of the `title{:ts}` and `author{:ts}`-Input, iterating over `form.title().errors(){:ts}` (or `form.author().errors(){:ts}`).
  - Only show the errors once the field was `touched(){:ts}`, e.g. wrap the `@for{:html}` in `@if (form.title().touched()) { ... }{:html}`.
  - Print the error's `message{:ts}` property inside the `<small>{:html}`-Tag.

> The Submit-Button is already disabled as long as the whole `form{:ts}` is not in a valid state via `[disabled]="form().invalid()"{:html}` from the previous task.
