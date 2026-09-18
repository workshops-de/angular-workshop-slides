In order to send the book to our Backend we need to wire our `BooksClient` (its `create` method already exists, from the earlier HTTP lesson) up to the form's submission.

- **Inject the service** Inject `BooksClient` inside of `BookCreateForm`.

---

- **Wire up the submission** Signal Forms handle submission themselves — you don't call a `submit()`-method from `(ngSubmit)` yourself. Instead, pass a third argument to `form()`: an options object with a `submission.action` callback. This callback is called automatically once the form is submitted and valid.
  - Inside `submission.action`, call `create()` on `BooksClient`, giving in the current `model()` value, and `await` the result (e.g. with `firstValueFrom` from `rxjs`).
  - The callback must return `null` on success, or a `{ kind, message }`-object to set as an error on the form.
