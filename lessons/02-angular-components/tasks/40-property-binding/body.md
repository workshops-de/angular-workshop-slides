Let's smoothly start with Angular's binding capabilities.

- **Add a style object** Open _src/app/books/book-card/book-card.ts_ and initialize a property `customStyle{:ts}` as a `signal{:ts}` holding an object with css-Styles _(see Hint for more information)_.
- **Bind it to the template** Switch to the template of the component and add a property binding to one HTML-Element of your choice.
  - Use a `[style]{:html}`-Binding.
  - Assign `customStyle(){:ts}` as value of the binding expression.

---

- **Show a cover** In _book-card.ts_ add a property `readonly placeholderCover = 'book-cover-placeholder.svg'{:ts}`. The image is already part of the project (_public/book-cover-placeholder.svg_). In _book-card.html_ add `<img [src]="placeholderCover" alt="" class="book-cover" />{:html}` as the first element inside the `book-card{:html}` element.

---

- **Check the result** Open [localhost:4200](http://localhost:4200). The book card shows a cover image and your custom style.
