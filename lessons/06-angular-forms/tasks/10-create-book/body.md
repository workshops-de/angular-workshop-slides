- **Generate `BookNewPage`** Create a new Component `BookNewPage` for the Book-Feature with `ng generate component books/book-new/book-new-page`.

---

- **Add the route** Configure a new Route inside the `book.routes.ts` File, displaying the `BookNewPage` (path: new).

---

- **Link to it** Add a link from `BooksPage` with `routerLink` to the `new` route.

---

- **Create the data model** Inside `book-new-page.ts`, create a `signal()` called `model` holding a plain object with the fields `isbn`, `title`, `subtitle`, `author`, and `abstract` (all empty strings).

---

- **Create the form** Call the `form()`-Function from `@angular/forms/signals`, passing in the `model` signal, and assign the result to a `form` property.

---

- **Import the directives** Add `FormRoot` and `FormField` from `@angular/forms/signals` to the `imports`-Array of `BookNewPage`.

---

- **Build the template** Inside the `book-new-page.html`-File:
  - Add a `<form>`-Tag and bind the created `form` Property to the `[formRoot]`-Directive
  - For each field of your model create one `<input>`-Tag and bind it to the matching field with the `[formField]`-Directive, e.g. `[formField]="form.isbn"`
  - Also add a Submit-Button with `type=submit`, disabled while the form is invalid via `[disabled]="form().invalid()"`

Run the application inside the Browser: You should see your form and be able to type into every field.
