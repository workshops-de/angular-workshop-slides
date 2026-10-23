ISBNs need to be unique — but we can only find that out by asking the Backend. Signal Forms support this via `validateHttp(){:ts}`, a helper that fires an HTTP request whenever the field's value changes and turns the result into a validation error.

---

- **Create the validator file** Create a file _isbn.ts_ inside the _books/validators_ folder.

---

- **Write the validator** Create a function `uniqueIsbn(path: SchemaPath<string>): void{:ts}` that calls `validateHttp(){:ts}` from `@angular/forms/signals`, passing in the `path{:ts}` and an options object with:
  - `request{:ts}`: a function `({ value }) => ...{:ts}` returning the URL to check: _http://localhost:4730/books/_ followed by `value(){:ts}`.
  - `onSuccess{:ts}`: called when the request resolves. A successful response means a book with that ISBN already exists, so return an error object, e.g. `{ kind: 'duplicateIsbn', message: 'This ISBN already exists' }{:ts}`.
  - `onError{:ts}`: called when the request fails. Our Backend answers with a `404` (`HttpErrorResponse{:ts}`) when no book with that ISBN exists — in that case return `null{:ts}` (no error). For any other error, return an error object of your choice.

---

- **Wire it up** In _book-create-form.ts_ call `uniqueIsbn(schemaPath.isbn){:ts}` inside the schema function of `BookCreateForm{:ts}`, right after the `required(){:ts}`-call for `isbn{:ts}`.

---

- **Show the pending state** While the request is in flight, `form.isbn().pending(){:ts}` is `true{:ts}`. In _book-create-form.html_ use it to show a _Checking ISBN…_ message beneath the ISBN-Input, instead of the usual error list.

---

- **Check the result** Type the ISBN of an existing book (e.g. from the book list) into the ISBN field. You briefly see _Checking ISBN…_, then the message _This ISBN already exists_. A new ISBN shows no error.
