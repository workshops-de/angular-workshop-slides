Now, it is time to feed our component with data using an `input()`-Binding.

- **Add an input signal** Open `src/app/books/book-card/book-card.ts`, add a property `content` and use the `input()` signal function with type `any` (do not forget to add the import from `@angular/core`). Switch to the template of _BookCard_ component and bind the values coming with `content` using a binding expression (e.g. `{{ content().title }}`).

---

- **Provide a book to bind** Switch to `src/app/app.ts` and initialize a property `book` as object with the properties _title_, _author_, _abstract_. Switch to the template of _App_ and bind the property `book` to the component `app-book-card` using its `input()`-binding **[content]**.

<iframe src="https://docs.google.com/presentation/d/1KJMDvEUIWDHluMPLffiBnadVSO2IElTAs7jPsMadehw/embed#slide=id.ga8afa0fa9e_0_24" height="800px" width="100%"></iframe>
