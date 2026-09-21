Reading data is only half the story. Let's add the missing mutations to `BooksClient{:ts}` and wire up deleting a book through the API.

---

- **Prepare `create{:ts}`, `update{:ts}` and `delete{:ts}` methods** In _books-client.ts_ inject `HttpClient{:ts}` via `inject(){:ts}` and add three methods that mirror the REST API: `create(book: Partial<Book>): Observable<Book>{:ts}` (`http.post<Book>(){:ts}` to _/books_), `update(isbn: string, book: Partial<Book>): Observable<Book>{:ts}` (`http.put<Book>(){:ts}` to _/books/:isbn_) and `delete(isbn: string): Observable<void>{:ts}` (`http.delete<void>(){:ts}` to _/books/:isbn_), all relative to the base URL. Note how `HttpClient{:ts}` and `httpResource{:ts}` live side by side in the same client. `create{:ts}` and `update{:ts}` will be wired up later once we build the forms - for now, `BooksClient{:ts}` just offers them.

---

- **Wire the delete action** In _books-page.ts_ turn `deleteBook(book){:ts}` into an `async{:ts}` method: ask for confirmation with `window.confirm(){:ts}` (message: _Delete "&lt;title&gt;"?_), `await{:ts}` the `delete(){:ts}` call via `lastValueFrom(...){:ts}` and then refresh the book list (`booksResource.reload(){:ts}`).

---

- **Check the result** Click _Delete_ on a card and confirm the dialog - the book disappears and stays gone after a page reload.
