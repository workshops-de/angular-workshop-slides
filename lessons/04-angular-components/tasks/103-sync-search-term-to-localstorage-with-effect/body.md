The search term is lost on every reload. An `effect` lets us react to signal changes and run side effects - here: persisting the value to `localStorage`.

---

- **Seed the signal from `localStorage`** Open _books-page.ts_ and change the `searchTerm` signal so its initial value comes from `localStorage`: `signal(localStorage.getItem('books.searchTerm') ?? '')`. The initial value is read once from an imperative, non-reactive API.

---

- **Persist the search term with `effect`** Add a `constructor` to `BooksPage` and register an `effect`. Inside the callback read `searchTerm()` and write it back via `localStorage.setItem('books.searchTerm', this.searchTerm())`.

---

- **Check the result** Open the browser at [localhost:4200](http://localhost:4200), type a search term and reload the page. The filter input should keep its value.
