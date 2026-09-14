`BookCreatePage`/`BookCreateForm` already exist (you copied them from `workshop-support` in the router lesson) and are already wired up via routing — but the form itself doesn't do anything yet. Let's fix that with Signal Forms.

- **Create the data model** Inside `book-create-form.ts`, create a `signal()` called `model` holding a plain object with the fields `isbn`, `title`, `subtitle`, `author`, and `abstract` (all empty strings).

---

- **Create the form** Call the `form()`-Function from `@angular/forms/signals`, passing in the `model` signal, and assign the result to a `form` property.

---

- **Import the directives** Add `FormRoot` and `FormField` from `@angular/forms/signals` to the `imports`-Array of `BookCreateForm`.

---

- **Wire up the template** Inside `book-create-form.html`:
  - Bind the created `form` Property to the `<form>`-Tag's `[formRoot]`-Directive.
  - For each field of your model, bind its `<input>`-Tag to the matching field with the `[formField]`-Directive, e.g. `[formField]="form.isbn"` (replacing the previous plain `name="isbn"` attribute).
  - Disable the existing Submit-Button while the form is invalid via `[disabled]="form().invalid()"`.

Run the application inside the Browser: You should see your form and be able to type into every field.
