## Handle a duplicate ISBN from the server

`uniqueIsbn(){:ts}` checks the ISBN while you type. But between the check and the click on _Save_, someone else can create a book with the same ISBN. The Backend has the final word: since _bookmonkey-api_ 5, `POST /books{:bash}` answers a duplicate ISBN with `409 Conflict{:bash}`. Right now the form shows the generic _Failed to create book_ for that.

- **Use the field parameter** `submission.action{:ts}` receives the form's field tree as its first parameter: `action: async field => { ... }{:ts}`.
- **Catch the 409** In the `catch{:ts}`-block of the action, check `error instanceof HttpErrorResponse && error.status === 409{:ts}` (import `HttpErrorResponse{:ts}` from `@angular/common/http`).
- **Show it at the ISBN field** Return the error with a `fieldTree{:ts}`: `{ kind: 'duplicateIsbn', message: 'This ISBN already exists', fieldTree: field.isbn }{:ts}`. Signal Forms attach it to that field, so it appears in the error list below the ISBN input instead of on the whole form. Keep the generic `server{:ts}`-error for all other failures.
- **Check the result** Open the create page in two tabs and enter the same new ISBN in both. Save in the first tab, then in the second. The second tab shows _This ISBN already exists_ at the ISBN field.
