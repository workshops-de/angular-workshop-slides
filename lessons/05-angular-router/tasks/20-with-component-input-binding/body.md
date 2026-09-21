- **Copy the prepared `BookDetailPage{:ts}`** Copy the folders `book-detail-page` and `book-detail` from `workshop-support/books/` into `src/app/books/`.
- **Add the route** Open `app.routes.ts` and add the route for the details view: `books/detail/:isbn`, displaying `BookDetailPage{:ts}`.

---

- **Navigate from `BooksPage{:ts}`** Open `BooksPage{:ts}` and inject the `Router{:ts}`-Injectable. Use the router in the method `goToBookDetails{:ts}`, to navigate to the details view (`this.router.navigate(['/books', 'detail', book.isbn]){:ts}`).

---

- **Enable Component Input Binding** Add `withComponentInputBinding(){:ts}` as a second argument to `provideRouter(routes, ...){:ts}` in `app.config.ts`.
- **Read the route param as an input** Inside `BookDetailPage{:ts}`, declare `readonly isbn = input('');{:ts}`. Thanks to Component Input Binding, Angular automatically sets this input to the current value of the `:isbn` route param — no `ActivatedRoute{:ts}` needed.

---

- **Load the book** Load the book with `` httpResource<Book>(() => `http://localhost:4730/books/${this.isbn()}`){:ts} `` and expose it (e.g. via a `computed{:ts}`).
- **Build the template** Pass the loaded book into `<app-book-detail [book]="book()" />{:html}`, guarded by `@if (book(); as book) { ... }{:html}`.
