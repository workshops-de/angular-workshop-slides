It is time to allow our component to communicate with other components.

- **Add output signals** Open _src/app/books/book-card/book-card.ts_ and initialize the properties `detailClick{:ts}` and `deleteClick{:ts}` with an `output(){:ts}` signal. Type both `output(){:ts}` signals to accept a `Book{:ts}` as event payload.
  - Make sure `output{:ts}` is imported from `@angular/core`.
- **Emit the events** Emit the `detailClick{:ts}`-Event within the `handleDetailClick{:ts}` method. Bind a new method `handleDeleteClick($event){:ts}` to the click of the _Delete_ button and emit `deleteClick{:ts}` from there. Prevent the default behaviour here as well.

---

- **Bind the outputs** Switch to _src/app/books/books-page/books-page.html_ and bind the `detailClick{:ts}`-Event of _<app-book-card>_ to a method `goToBookDetails($event){:ts}` and the `deleteClick{:ts}`-Event to a method `deleteBook($event){:ts}`.
- **Implement the handlers** In _books-page.ts_ implement `goToBookDetails($event){:ts}` and `deleteBook($event){:ts}` and log the book passed by _<app-book-card>_.

<iframe src="https://docs.google.com/presentation/d/1KJMDvEUIWDHluMPLffiBnadVSO2IElTAs7jPsMadehw/embed#slide=id.gab308489f3_0_122" height="700px" width="100%"></iframe>
