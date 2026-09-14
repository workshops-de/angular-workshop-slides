Reading data is only half the story. Let's remove a book through the API and refresh the list afterwards.

---

- **Add a `delete` method** In _books-client.ts_ inject `HttpClient` via `inject()` and add `delete(isbn: string): Observable<void>` that sends `http.delete<void>(\`${baseUrl}/books/${isbn}\`)`. Note how `HttpClient` and `httpResource` live side by side in the same client.

---

- **Wire the delete action** In _books-page.ts_ turn `deleteBook(book)` into an `async` method: ask for confirmation with `window.confirm(\`Delete "${book.title}"?\`)`, `await` the `delete()` call via `lastValueFrom(...)` and then refresh the book list (`booksResource.reload()`).

---

- **Check the result** Click _Delete_ on a card and confirm the dialog - the book disappears and stays gone after a page reload.
