In order to send the book to our Backend we need to wire our `BooksClient{:ts}` (its `create{:ts}` method already exists, from the earlier HTTP lesson) up to the form's submission.

- **Inject the service** Inject `BooksClient{:ts}` inside of `BookCreateForm{:ts}`.

---

- **Wire up the submission** Signal Forms handle submission themselves — you don't call a `submit(){:ts}`-method from `(ngSubmit){:html}` yourself. Instead, pass a third argument to `form(){:ts}`: an options object with a `submission.action{:ts}` callback. This callback is called automatically once the form is submitted and valid.
  - Inside `submission.action{:ts}`, call `create(){:ts}` on `BooksClient{:ts}`, giving in the current `model(){:ts}` value, and `await{:ts}` the result (e.g. with `firstValueFrom{:ts}` from `rxjs`).
  - The callback must return `null{:ts}` on success, or a `{ kind, message }{:ts}`-object to set as an error on the form.
