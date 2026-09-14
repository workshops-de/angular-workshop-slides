Time to swap the hard-coded books for real data. Angular's `httpResource` gives us a reactive resource backed by an HTTP call - no manual subscription management needed.

---

- **Start the API** Start our HTTP-Server `bookmonkey-api` in your shell.

---

- **Provide the HttpClient** Import `provideHttpClient` in _app.config.ts_ and add it to the `providers` array.

---

- **Extend the `Book` interface** Open _book.ts_ and extend `Book` with the fields the API returns, e.g. `isbn`, `cover`, `subtitle`, `price`, `numPages` and `publishedAt`. Most of them are optional - only `isbn` and `title` stay required.

---

- **Load data via `httpResource`** In _books-client.ts_ change `getAll()` to return an `httpResource<Book[]>`. Point it at `http://localhost:4730/books`, pass `_start`, `_end`, `_sort` and `_order` as `params` to page and sort the result, and set `defaultValue: []` so the list is never `undefined`.

---

- **Consume the resource in `BooksPage`** Rename `books` to `booksResource` and read the loaded data via `booksResource.value()` inside `booksComputed`.

---

- **Show loading and error state** In _books-page.html_ display a short message while `booksResource.isLoading()` and the error message when `booksResource.error()` is set.

---

- **Show the real cover** In _book-card.html_ use `currentBook.cover || placeholderCover` as the image `src`, so books without a cover still fall back to the placeholder.

---

- **Track by isbn** Use the `isbn` property of `Book` as key for the track function (`@for`) in the `BooksPage` template.

---

- **Check the result** Start the app, confirm the books now come from the API and that the loading message briefly appears on a reload.
