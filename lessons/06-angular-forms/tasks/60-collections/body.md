A book can have more than one author. Let's add a `coAuthors{:ts}`-Collection next to the existing, single `author{:ts}`-Field. Signal Forms have a dedicated helper, `applyEach(){:ts}`, to apply a schema to every item of an array field.

---

- **Extend the model** In _book-create-form.ts_ add a `coAuthors: string[]{:ts}`-Field (an empty array) and a `cover{:ts}`-Field (an empty string) to your `model{:ts}`, so the model mirrors the `Book{:ts}` payload.

---

- **Extend the schema** Inside the schema function, add `applyEach(schemaPath.coAuthors, coAuthor => { ... }){:ts}`. Inside the callback call `required(coAuthor, { ... }){:ts}` and `validAuthorName(coAuthor){:ts}` — every co-author entry gets the same rules as the primary `author{:ts}`.

---

- **Build the template** In _book-create-form.html_ add a `<fieldset>{:html}` between the Author- and the Abstract-Field:
  - Iterate with `@for{:html}` over `form.coAuthors{:ts}` (one form field per entry of `coAuthors{:ts}`).
  - Render one `<input>{:html}` per co-author, bound via `[formField]{:html}`, plus its own error-`@for{:html}`-Block.
  - Add an `@empty{:html}`-Block showing a short hint when there are no co-authors yet.

---

- **Add and remove co-authors** Let the user change the list:
  - In _book-create-form.ts_ add the methods `addCoAuthor(){:ts}` and `removeCoAuthor(index: number){:ts}`. Both update the `coAuthors{:ts}`-Array on the `model{:ts}` signal, e.g. `this.model.update(m => ({ ...m, coAuthors: [...m.coAuthors, ''] })){:ts}`.
  - In _book-create-form.html_ add a Button that calls `addCoAuthor(){:ts}`, and one Button per co-author-Input that calls `removeCoAuthor(index){:ts}`. The index comes from the `$index{:ts}` of `@for{:html}`.

> The model already mirrors the `Book{:ts}` payload one-to-one, so `submission.action{:ts}` can keep sending `this.model(){:ts}` as-is — no reshaping needed.

---

- **Check the result** Add two co-authors, remove one again and save the book. A co-author with a digit in the name shows the same error as the main author.
