The search term is lost on every reload. An `effect{:ts}` lets us react to signal changes and run side effects - here: persisting the value to `localStorage{:ts}`.

---

- **Seed the signal from `localStorage{:ts}`** Open _books-page.ts_ and change the `searchTerm{:ts}` signal so its initial value comes from `localStorage{:ts}`: `signal(localStorage.getItem('books.searchTerm') ?? ''){:ts}`. The initial value is read once from an imperative, non-reactive API.

---

- **Persist the search term with `effect{:ts}`** Add a `constructor{:ts}` to `BooksPage{:ts}` and register an `effect{:ts}`. Inside the callback read `searchTerm(){:ts}` and write it back via `localStorage.setItem('books.searchTerm', this.searchTerm()){:ts}`.

---

- **Check the result** Open the browser at [localhost:4200](http://localhost:4200), type a search term and reload the page. The filter input should keep its value.
