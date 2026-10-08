- **Copy the prepared `BookDetailPage{:ts}`** Copy the folders `book-detail-page` and `book-detail` from `workshop-support/books/` into `src/app/books/`.
- **Add the route** Open `app.routes.ts` and add the route for the details view: `books/detail/:isbn`, displaying `BookDetailPage{:ts}`.

---

- **Navigate from `BooksPage{:ts}`** Open `BooksPage{:ts}` and inject the `Router{:ts}`-Injectable. Use the router in the method `goToBookDetails{:ts}`, to navigate to the details view (`this.router.navigate(['/books', 'detail', book.isbn]){:ts}`).

---

- **Enable Component Input Binding** Add `withComponentInputBinding(){:ts}` as a second argument to `provideRouter(routes, ...){:ts}` in `app.config.ts`.
- **Read the route param as an input** Inside `BookDetailPage{:ts}`, declare `readonly isbn = input('');{:ts}`. Thanks to Component Input Binding, Angular automatically sets this input to the current value of the `:isbn` route param — no `ActivatedRoute{:ts}` needed.

---

- **Load the book** Inject `BooksClient{:ts}` into `BookDetailPage{:ts}` and call its method `getByIsbn(){:ts}` with the `isbn` input. Store the returned resource in a property `bookResource{:ts}`.
- **Build the template** Pass the loaded book (`bookResource.value(){:ts}`) into `<app-book-detail [book]="book" />{:html}`, guarded by `@if (bookResource.value(); as book) { ... }{:html}`.
