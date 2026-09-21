Since we add more and more books to our list, a filter is helpful to focus the book you want to know more about.

---

- **The Book filter control** In _app.ts_ add a `signal{:ts}` property called `searchTerm{:ts}`. Switch to _app.html_ and add an _<input>_-Field acting as search field. Handle its `(input){:html}`-Event by setting the signal directly: `searchTerm.set($event.target.value){:ts}`.

---

- **Derive the filtered books with `computed{:ts}`** Open _app.ts_ and add a `computed{:ts}` property called `booksComputed{:ts}`. Inside its callback, read `searchTerm(){:ts}` and the `books{:ts}` list, and return only the books that match the search term. Don't write the matching logic yourself: import the pre-defined helper `bookMatches{:ts}` from `@workshop-support` and use it as `bookMatches(book, searchTerm){:ts}` to decide whether a book matches.

---

- **Use `booksComputed{:ts}` in the template** Switch to _app.html_ and change the `@for{:html}`-expression to iterate over `booksComputed(){:ts}` instead of `books{:ts}`.

---

- **Check the result** Open the browser at [localhost:4200](http://localhost:4200) and check if the filter works as expected.
