Now, it is time to feed our component with data using an `input(){:ts}`-Binding.

---

- **Add an input signal** Open _src/app/books/book-card/book-card.ts_, add a property `book{:ts}` and use the `input(){:ts}` signal function with type `any{:ts}` (do not forget to add the import from `@angular/core`).

---

- **Read the input in the template** Switch to the template of _BookCard_ component. Store the current value in a template variable via `@let currentBook = book();{:html}` and replace the static title, author and published date with binding expressions (e.g. `{{ currentBook.title }}{:html}`).

---

- **Provide a book to bind** Switch to _src/app/books/books-page/books-page.ts_ and initialize a property `book{:ts}` as object with the properties _title_, _author_, _publishedAt_ (a `Date{:ts}`). Switch to the template of _BooksPage_ (_books-page.html_) and bind the property `book{:ts}` to the component `app-book-card{:html}` using its `input(){:ts}`-binding `[book]{:html}`.

---

- **Check the result** Open [localhost:4200](http://localhost:4200). The book card now shows the title, author and published date of the book from _BooksPage_.

<iframe src="https://docs.google.com/presentation/d/1KJMDvEUIWDHluMPLffiBnadVSO2IElTAs7jPsMadehw/embed#slide=id.ga8afa0fa9e_0_24" height="800px" width="100%"></iframe>
