- **Create the child routes file** Create a new file _book.routes.ts_ inside the _books_ folder to configure child routes.

---

- **Move the book routes** Transfer the routes _books_, _books/create_ & _books/detail_ from _app.routes.ts_ to _book.routes.ts_.
  - Pay attention to the hints: The paths will slightly change.

---

- **Lazy load the book routes** Add a lazy loaded route for the path `books{:ts}` loading the _book.routes.ts_ in _app.routes.ts_.

---

- **Lazy load the book details route** We can be even more lazy — `BookDetailPage{:ts}` might not need to be loaded up front. Use `loadComponent{:ts}` to load it lazily.

---

- **Check the result**
  - Make sure that the compiler in your terminal shows _lazy chunk files_ in the output.
  - Open your app in the browser, open the Developer Tools -> Network Tab and check the chunk bundles in the list of network requests.
  - Verify that a separate chunk is generated and loaded for `BookDetailPage{:ts}`.
