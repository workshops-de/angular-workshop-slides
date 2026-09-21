Time to swap the hard-coded books for real data. Angular's `httpResource{:ts}` gives us a reactive resource backed by an HTTP call - no manual subscription management needed.

---

- **Start the API** Start our HTTP-Server `bookmonkey-api` in your shell.

---

- **Provide the HttpClient** Import `provideHttpClient{:ts}` in _app.config.ts_ and add it to the `providers{:ts}` array.

---

- **Extend the `Book{:ts}` interface** Open _book.ts_ and extend `Book{:ts}` with the fields the API returns, e.g. `isbn{:ts}`, `cover{:ts}`, `subtitle{:ts}`, `price{:ts}`, `numPages{:ts}` and `publishedAt{:ts}`. Most of them are optional - only `isbn{:ts}` and `title{:ts}` stay required.

---

- **Load data via `httpResource{:ts}`** In _books-client.ts_ change `getAll(){:ts}` to return an `httpResource<Book[]>{:ts}`. Point it at `http://localhost:4730/books`, pass `_start{:ts}`, `_end{:ts}`, `_sort{:ts}` and `_order{:ts}` as `params{:ts}` to page and sort the result, and set `defaultValue: []{:ts}` so the list is never `undefined{:ts}`.

---

- **Consume the resource in `BooksPage{:ts}`** Rename `books{:ts}` to `booksResource{:ts}` and read the loaded data via `booksResource.value(){:ts}` inside `booksComputed{:ts}`.

---

- **Show loading and error state** In _books-page.html_ display a short message while `booksResource.isLoading(){:ts}` and the error message when `booksResource.error(){:ts}` is set.

---

- **Show the real cover** In _book-card.html_ use `currentBook.cover || placeholderCover{:ts}` as the image `src`, so books without a cover still fall back to the placeholder.

---

- **Track by isbn** Use the `isbn{:ts}` property of `Book{:ts}` as key for the track function (`@for{:html}`) in the `BooksPage{:ts}` template.

---

- **Check the result** Start the app, confirm the books now come from the API and that the loading message briefly appears on a reload.
