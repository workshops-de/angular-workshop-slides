A book can have more than one author. Let's add a `coAuthors{:ts}`-Collection next to the existing, single `author{:ts}`-Field. Signal Forms have a dedicated helper, `applyEach(){:ts}`, to apply a schema to every item of an array field.

- **Extend the model** Add a `coAuthors: string[]{:ts}`-Field to your `model{:ts}` (an empty array) and a `cover{:ts}`-Field (an empty string), so the model mirrors the `Book{:ts}` payload.

---

- **Extend the schema** Inside the schema function, add `applyEach(schemaPath.coAuthors, coAuthor => { required(coAuthor, {...}); validAuthorName(coAuthor); }){:ts}` — this validates every co-author entry with the same rules as the primary `author{:ts}`.

---

- **Build the template** Iterate with `@for{:html}` over `form.coAuthors{:ts}` (the array of per-item form fields, one per entry of `coAuthors{:ts}`) and render one `<input>{:html}` (bound via `[formField]{:html}`) per co-author, plus its own error-`@for{:html}`-Block. Wrap the list in a `<fieldset>{:html}` between the Author- and Abstract-Field and add an `@empty{:html}`-Block showing a short hint when there are no co-authors yet.

---

- **Add and remove co-authors** Add `addCoAuthor(){:ts}` and `removeCoAuthor(index: number){:ts}` methods on `BookCreateForm{:ts}` that update the `coAuthors{:ts}`-Array on the `model{:ts}` signal (e.g. `this.model.update(m => ({ ...m, coAuthors: [...m.coAuthors, ''] })){:ts}`).
- Add a Button for adding a new co-author, and one Button per rendered co-author-Input for removing it (calling `removeCoAuthor(index){:ts}`; the index comes from the `@for{:html}`'s `$index{:ts}`).

> The model already mirrors the `Book{:ts}` payload one-to-one, so `submission.action{:ts}` can keep sending `this.model(){:ts}` as-is — no reshaping needed.
