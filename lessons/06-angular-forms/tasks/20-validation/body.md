Let's add some form validation! Signal Forms define validation next to the model, via a **schema function** — the second argument to `form(){:ts}`. Inside it you get a `schemaPath{:ts}` that mirrors your model's shape, and you attach validators like `required(){:ts}` to individual paths (e.g. `schemaPath.isbn{:ts}`).

---

- **Add a schema function** In _book-create-form.ts_ insert a function `schemaPath => { ... }{:ts}` as the second argument to `form(){:ts}`. The options object with your `submission{:ts}` placeholder moves to the third position.

---

- **Add validators** Inside that function call `required(schemaPath.isbn, { message: '...' }){:ts}` for `isbn{:ts}`, `title{:ts}` and `author{:ts}`. Import `required{:ts}` from `@angular/forms/signals`.

---

- **Show validation errors** In _book-create-form.html_ add some template logic for fields in an error state:
  - Add a `@for{:html}`-Block with a `<small class="field-error">{:html}`-Tag beneath the `<input>{:html}`-Tags of `isbn{:ts}`, `title{:ts}` and `author{:ts}`, iterating over `form.isbn().errors(){:ts}` (or `form.title().errors(){:ts}`, `form.author().errors(){:ts}`).
  - Only show the errors once the field was `touched(){:ts}`, e.g. wrap the `@for{:html}` in `@if (form.title().touched()) { ... }{:html}`.
  - Print the error's `message{:ts}` property inside the `<small>{:html}`-Tag.

> The Save-Button is already disabled as long as the whole `form{:ts}` is not valid, via `[disabled]="form().invalid()"{:html}` from the previous task.

---

- **Check the result** Open the create page, click into a field and leave it empty. The error message appears below the field, and the Save-Button stays disabled until all required fields are filled.
