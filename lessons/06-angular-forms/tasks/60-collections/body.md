A book can have more than one author. Let's add a `coAuthors`-Collection next to the existing, single `author`-Field. Signal Forms have a dedicated helper, `applyEach()`, to apply a schema to every item of an array field.

- **Extend the model** Add a `coAuthors: string[]`-Field to your `model` (an empty array).

---

- **Extend the schema** Inside the schema function, add `applyEach(schemaPath.coAuthors, coAuthor => { required(coAuthor, {...}); validAuthorName(coAuthor); })` — this validates every co-author entry with the same rules as the primary `author`.

---

- **Build the template** Iterate with `@for` over `form.coAuthors` (the array of per-item form fields, one per entry of `coAuthors`) and render one `<input>` (bound via `[formField]`) per co-author, plus its own error-`@for`-Block. Add an `@empty`-Block showing a short hint when there are no co-authors yet.

---

- **Add and remove co-authors** Add `addCoAuthor()` and `removeCoAuthor(index: number)` methods on `BookCreateForm` that update the `coAuthors`-Array on the `model` signal (e.g. `this.model.update(m => ({ ...m, coAuthors: [...m.coAuthors, ''] }))`).
- Add a Button for adding a new co-author, and one Button per rendered co-author-Input for removing it (calling `removeCoAuthor(index)`; the index comes from the `@for`'s `$index`).

> The model already mirrors the `Book` payload one-to-one, so `submission.action` can keep sending `this.model()` as-is — no reshaping needed.
