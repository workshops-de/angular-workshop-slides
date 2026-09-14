Since we add more and more books to our list, a filter is helpful to focus the book you want to know more about.

---

- **The Book filter control** In _app.ts_ add a `signal` property called `searchTerm`. Switch to _app.html_ and add an _<input>_-Field acting as search field. Handle its `(input)`-Event by setting the signal directly: `searchTerm.set($event.target.value)`.

---

- **Derive the filtered books with `computed`** Open _app.ts_ and add a `computed` property called `booksComputed`. Inside its callback, read `searchTerm()` and the `books` list, and return only the books whose **title** contains the search term.

---

- **Use `booksComputed` in the template** Switch to _app.html_ and change the `@for`-expression to iterate over `booksComputed()` instead of `books`.

---

- **Check the result** Open the browser at [localhost:4200](http://localhost:4200) and check if the filter works as expected.
