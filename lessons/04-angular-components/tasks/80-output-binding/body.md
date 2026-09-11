It is time to allow our component to communicate with other components.

- **Add an output signal** Open _src/app/books/book-card/book-card.ts_ and initialize a property `detailClick` with an `output()` signal. Type the `output()` signal to accept a `Book` as event payload.
  - Make sure `output` is imported from `@angular/core`.
- **Emit the event** Emit the `detailClick`-Event within the `handleDetailClick` method.

---

- **Bind the output** Switch to _src/app/app.html_ and bind to the `detailClick`-Event of _<app-book-card>_ to a method `goToBookDetails($event)`.
- **Implement the handler** Implement `goToBookDetails($event)` and log the book passed by _<app-book-card>_.

<iframe src="https://docs.google.com/presentation/d/1KJMDvEUIWDHluMPLffiBnadVSO2IElTAs7jPsMadehw/embed#slide=id.gab308489f3_0_122" height="700px" width="100%"></iframe>
