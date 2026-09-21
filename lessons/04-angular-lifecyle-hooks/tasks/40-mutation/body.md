Reading data is only half the story. Let's add the missing mutations to `BooksClient` and wire up deleting a book through the API.

---

- **Prepare `create`, `update` and `delete` methods** In _books-client.ts_ inject `HttpClient` via `inject()` and add three methods that mirror the REST API: `create(book: Partial<Book>): Observable<Book>` (`http.post<Book>(\`${baseUrl}/books\`, book)`), `update(isbn: string, book: Partial<Book>): Observable<Book>` (`http.put<Book>(\`${baseUrl}/books/${isbn}\`, book)`) and `delete(isbn: string): Observable<void>` (`http.delete<void>(\`${baseUrl}/books/${isbn}\`)`). Note how `HttpClient`and`httpResource`live side by side in the same client.`create`and`update`will be wired up later once we build the forms - for now,`BooksClient` just offers them.

---

- **Wire the delete action** In _books-page.ts_ turn `deleteBook(book)` into an `async` method: ask for confirmation with `window.confirm(\`Delete "${book.title}"?\`)`, `await`the`delete()`call via`lastValueFrom(...)` and then refresh the book list (`booksResource.reload()`).

---

- **Check the result** Click _Delete_ on a card and confirm the dialog - the book disappears and stays gone after a page reload.
