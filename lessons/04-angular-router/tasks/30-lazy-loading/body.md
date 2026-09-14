- **Create the child routes file** Create a new file `book.routes.ts` inside the `books` folder to configure child routes.
- Transfer the routes _books_, _books/create_ & _books/detail_ from _app.routes.ts_ to `book.routes.ts`.
  - Pay attention to the hints: The paths will slightly change.
- Add a lazy loaded route for the path `books` loading the `book.routes.ts` in _app.routes.ts_.
- Make sure that the compiler in your terminal shows _lazy chunk files_ in the output.
- Open your app in the browser, open the Developer Tools -> Network Tab and check the chunk bundles in the list of network requests.

---

- **Lazy load the book details route** We can be even more lazy — `BookDetailPage` might not need to be loaded up front. Use `loadComponent` to load it lazily.
- Verify that a separate chunk is generated and loaded for `BookDetailPage`.
