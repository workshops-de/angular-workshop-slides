A book can have more than one author. Signal Forms have a dedicated helper, `applyEach()`, to apply a schema to every item of an array field.

1. Change the `author: string`-Field of your `model` to an `authors: string[]`-Field (an array with one empty string as the initial value).
2. Inside the schema function, replace the `required`/`validAuthorName`-Calls for `author` with `applyEach(schemaPath.authors, author => { required(author, {...}); validAuthorName(author); })`.
3. Inside the template, iterate with `@for` over `form.authors` (the array of per-item form fields, one per entry of `authors`) and render one `<input>` (bound via `[formField]`) per Author.
4. Add `addAuthor()` and `deleteAuthor(index: number)` methods on `BookNewPage` that update the `authors`-Array on the `model` signal (e.g. `this.model.update(m => ({ ...m, authors: [...m.authors, ''] }))`).
5. Add a Button for adding a new Author, and one Button per rendered Author-Input for removing it (calling `deleteAuthor(index)`; the index comes from the `@for`'s `$index`).
6. Our Backend cannot handle multiple authors — in the submission `action`, still only send the first entry of `authors` as `author` when calling `create()`.
