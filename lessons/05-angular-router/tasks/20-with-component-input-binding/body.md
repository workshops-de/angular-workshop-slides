- **Copy the prepared `BookDetailPage{:ts}`** Copy the folders _book-detail-page_ and _book-detail_ from _workshop-support/books/_ into _src/app/books/_.

---

- **Add the route** Open _app.routes.ts_ and add the route for the details view: _books/detail/:isbn_, displaying `BookDetailPage{:ts}`.

---

- **Navigate from `BooksPage{:ts}`** Open `BooksPage{:ts}` and inject the `Router{:ts}`-Injectable. Use the router in the method `goToBookDetails{:ts}`, to navigate to the details view (`this.router.navigate(['/books', 'detail', book.isbn]){:ts}`).

---

- **Enable Component Input Binding** Add `withComponentInputBinding(){:ts}` as a second argument to `provideRouter(routes, ...){:ts}` in _app.config.ts_.

---

- **Read the route param as an input** Inside `BookDetailPage{:ts}`, declare `readonly isbn = input.required<string>();{:ts}`. Thanks to Component Input Binding, Angular automatically sets this input to the current value of the _:isbn_ route param — no `ActivatedRoute{:ts}` needed. The input is `required{:ts}` because the route always provides _:isbn_.

---

- **Load the book** Inject `BooksClient{:ts}` into `BookDetailPage{:ts}` and call its method `getByIsbn(){:ts}` with the `isbn{:ts}` input. Store the returned resource in a property `bookResource{:ts}`.

---

- **Build the template** Pass the loaded book (`bookResource.value(){:ts}`) into `<app-book-detail [book]="book" />{:html}`, guarded by `@if (bookResource.value(); as book) { ... }{:html}`.

---

- **Check the result** Click _More_ on a book card in the list. You land on the detail page of that book.
