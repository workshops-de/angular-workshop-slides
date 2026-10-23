The markup for a single co-author row (input, remove-button, error-list) is starting to clutter _book-create-form.html_. Signal Forms let you extract it into its own component by implementing `FormValueControl{:ts}` — then `[formField]{:html}` can bind to it just like to a plain `<input>{:html}`.

---

- **Generate `CoAuthorInput{:ts}`** Create a new component with `ng generate component books/co-author-input{:bash}`.

---

- **Implement `FormValueControl<string>{:ts}`** In _co-author-input.ts_ add `implements FormValueControl<string>{:ts}` (from `@angular/forms/signals`) to the class. It requires:
  - `value = model('');{:ts}` — the two-way bound value.
  - `touched = input(false);{:ts}`, `disabled = input(false);{:ts}`, `invalid = input(false);{:ts}` and `errors = input<readonly ValidationError[]>([]);{:ts}`
  - `touch = output<void>();{:ts}` — emitted whenever the control is blurred.

---

- **Add a `remove{:ts}`-Output** Add your own `remove = output<void>();{:ts}` for the remove-button.

---

- **Build the template** Move the input, the remove-button and the error-`@for{:html}`-Block from _book-create-form.html_ into _co-author-input.html_:
  - Bind the input's value and disabled state via `[value]{:html}` and `[disabled]{:html}`.
  - Update the value via `(input){:html}` and emit `touch{:ts}` on `(blur){:html}`.
  - Wire the remove-button's `(click){:html}` to `remove.emit(){:ts}`.

---

- **Use it in `BookCreateForm{:ts}`** In _book-create-form.html_ replace the markup of a co-author row with a single `<app-co-author-input [formField]="coAuthor" (remove)="removeCoAuthor(coAuthorIndex)" />{:html}`. Add `CoAuthorInput{:ts}` to the `imports{:ts}`-Array of `BookCreateForm{:ts}`.

---

- **Check the result** Open the create page: adding, editing and removing co-authors works exactly like before — just with much less markup in `BookCreateForm{:ts}`.
