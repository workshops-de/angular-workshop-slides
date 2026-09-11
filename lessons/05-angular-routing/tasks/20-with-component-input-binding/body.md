- **Generate `BookDetailPage`** Create a new Component `BookDetailPage` with the Angular CLI: `ng generate component books/book-detail/book-detail-page`.
- **Add the route** Open `app.routes.ts` and add the route for the details view: _books/detail/:isbn_.

---

- **Navigate from `BooksPage`** Open _BooksPage_ and inject the `Router`-Injectable. Use the router in the method `goToBookDetails`, to navigate to the details view.

---

- **Extend the client** Open _BooksClient_ and extend it, allowing to load a book with its ISBN (`getByIsbn(isbn: string)`).

---

- **Load the book in `BookDetailPage`** Open _BookDetailPage_ and inject both `ActivatedRoute` & `BooksClient`. Extract the ISBN from the route-`params` and use `BooksClient` to load the book.
- **Build the template** Setup a template displaying the book information.
  - You can reuse some parts of the _BookCard_'s template, if you like.
