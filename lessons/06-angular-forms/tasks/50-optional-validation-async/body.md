ISBNs need to be unique — but we can only find that out by asking the Backend. Signal Forms support this via `validateHttp()`, a helper that fires an HTTP request whenever the field's value changes and turns the result into a validation error.

- Create a file `isbn.ts` inside the `books/validators` folder.
- Create a function `uniqueIsbn(path: SchemaPath<string>): void` that calls `validateHttp()` from `@angular/forms/signals`, passing in the `path` and an options object with:
  - `request`: a function `({ value }) => ...` returning the URL to check, e.g. `` `http://localhost:4730/books/${value()}` ``
  - `onSuccess`: called when the request resolves — since a successful response means a book with that ISBN already exists, return an error object here, e.g. `{ kind: 'duplicateIsbn', message: 'This ISBN already exists' }`.
  - `onError`: called when the request fails. Our Backend answers with a `404` (`HttpErrorResponse`) when no book with that ISBN exists — in that case return `null` (no error). For any other error, return an error object of your choice.
- Call `uniqueIsbn(schemaPath.isbn)` inside the schema function of `BookNewPage`, right after the `required()`-call for `isbn`.
- While the request is in flight, `form.isbn().pending()` is `true` — use it in the template to show a "Checking ISBN…" message beneath the ISBN-Input, instead of the usual error list.
