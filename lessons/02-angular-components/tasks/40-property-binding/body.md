Let's smoothly start with Angular's binding capabilities.

- **Add a style object** Open _src/app/books/book-card/book-card.ts_ and initialize a property `customStyle{:ts}` as a `signal{:ts}` holding an object with css-Styles _(see Hint for more information)_.
- **Bind it to the template** Switch to the template of the component and add a property binding to one HTML-Element of your choice.
  - Use a `[style]{:html}`-Binding.
  - Assign `customStyle(){:ts}` as value of the binding expression.
