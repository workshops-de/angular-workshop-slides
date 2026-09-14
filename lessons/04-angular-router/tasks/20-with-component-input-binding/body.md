- **Copy the prepared `BookDetailPage`** Copy the folders `book-detail-page` and `book-detail` from `workshop-support/books/` into `src/app/books/`.
- **Add the route** Open `app.routes.ts` and add the route for the details view: `books/detail/:isbn`, displaying `BookDetailPage`.

---

- **Navigate from `BooksPage`** Open `BooksPage` and inject the `Router`-Injectable. Use the router in the method `goToBookDetails`, to navigate to the details view (`this.router.navigate(['/books', 'detail', book.isbn])`).

---

- **Enable Component Input Binding** Add `withComponentInputBinding()` as a second argument to `provideRouter(routes, ...)` in `app.config.ts`.
- **Read the route param as an input** Inside `BookDetailPage`, declare `readonly isbn = input('');`. Thanks to Component Input Binding, Angular automatically sets this input to the current value of the `:isbn` route param — no `ActivatedRoute` needed.

---

- **Load the book** Load the book with `httpResource<Book>(() => \`http://localhost:4730/books/${this.isbn()}\`)` and expose it (e.g. via a `computed`).
- **Build the template** Pass the loaded book into `<app-book-detail [book]="book()" />`, guarded by `@if (book(); as book) { ... }`.
