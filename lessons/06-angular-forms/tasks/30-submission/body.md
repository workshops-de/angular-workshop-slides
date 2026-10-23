In order to send the book to our Backend we need to wire our `BooksClient{:ts}` (its `create{:ts}` method already exists, from the earlier HTTP lesson) up to the form's submission.

- **Inject the service** Inject `BooksClient{:ts}` inside of `BookCreateForm{:ts}`.

---

- **Wire up the submission** Signal Forms handle submission themselves — you don't call a `submit(){:ts}`-method from `(ngSubmit){:html}` yourself. Instead, the `submission.action{:ts}` callback in the options object of `form(){:ts}` (the third argument since the validation task) is called automatically once the form is submitted and valid.
  - Replace the placeholder logging inside `submission.action{:ts}` with a call to `create(){:ts}` on `BooksClient{:ts}`, giving in the current `model(){:ts}` value, and `await{:ts}` the result (e.g. with `firstValueFrom{:ts}` from `rxjs`).
  - The callback must return `null{:ts}` on success, or a `{ kind, message }{:ts}`-object to set as an error on the form.

---

- **Tell the page that the book is saved** In the router lesson, `BookCreatePage{:ts}` got a hard-coded `hasUnsavedChanges = signal(true){:ts}` for the `canDeactivate{:ts}`-Guard. Now the form can tell the page when the book is saved:
  - In _book-create-form.ts_ add `readonly saved = output<void>();{:ts}` and call `this.saved.emit(){:ts}` right after a successful `create(){:ts}`.
  - In _book-create-page.html_ listen to it: `<app-book-create-form (saved)="hasUnsavedChanges.set(false)" />{:html}`.

> The guard stays simple: it asks as long as the book is not saved, even if you have not typed anything yet.

---

- **Check the result** Create a book. After saving you can leave the page without being asked. Without saving, the guard still asks.
