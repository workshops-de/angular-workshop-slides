`BookCreatePage{:ts}`/`BookCreateForm{:ts}` already exist (you copied them from `workshop-support` in the router lesson) and are already wired up via routing — but the form itself doesn't do anything yet. Let's fix that with Signal Forms.

- **Create the data model** Inside `book-create-form.ts`, create a `signal(){:ts}` called `model{:ts}` holding a plain object with the fields `isbn{:ts}`, `title{:ts}`, `subtitle{:ts}`, `author{:ts}`, and `abstract{:ts}` (all empty strings).

---

- **Create the form** Call the `form(){:ts}`-Function from `@angular/forms/signals`, passing in the `model{:ts}` signal, and assign the result to a `form{:ts}` property.
- **Add a placeholder submission** A form bound via `[formRoot]{:html}` needs to know what to do on submit. Pass an options object as second argument to `form(){:ts}` with a `submission.action{:ts}` callback that logs the current `model(){:ts}` to the console and returns `Promise.resolve(null){:ts}`. We replace it with a real request in a later task.

---

- **Import the directives** Add `FormRoot{:ts}` and `FormField{:ts}` from `@angular/forms/signals` to the `imports{:ts}`-Array of `BookCreateForm{:ts}`.

---

- **Wire up the template** Inside `book-create-form.html`:
  - Bind the created `form{:ts}` Property to the `<form>{:html}`-Tag's `[formRoot]{:html}`-Directive.
  - For each field of your model, bind its `<input>{:html}`-Tag to the matching field with the `[formField]{:html}`-Directive, e.g. `[formField]="form.isbn"{:html}` (replacing the previous plain `name="isbn"{:html}` attribute).
  - Disable the existing Submit-Button while the form is invalid via `[disabled]="form().invalid()"{:html}`.

Run the application inside the Browser: You should see your form and be able to type into every field. Clicking "Save" should log the model to the console.
