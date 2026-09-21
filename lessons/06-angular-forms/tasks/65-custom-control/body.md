The markup for a single co-author row (input, remove-button, error-list) is starting to clutter `book-create-form.html`. Signal Forms let you extract it into its own component by implementing `FormValueControl{:ts}` — then `[formField]{:html}` can bind to it just like to a plain `<input>{:html}`.

- **Generate `CoAuthorInput{:ts}`** Create a new Component with `ng generate component books/co-author-input{:bash}`.
- **Implement `FormValueControl<string>{:ts}`** Add `implements FormValueControl<string>{:ts}` (from `@angular/forms/signals`) to the class. It requires:
  - `value = model('');{:ts}` — the two-way bound value.
  - `touched = input(false);{:ts}`, `disabled = input(false);{:ts}`, `invalid = input(false);{:ts}`, `errors = input<readonly ValidationError[]>([]);{:ts}`
  - `touch = output<void>();{:ts}` — emitted whenever the control is blurred.
- **Add a `remove{:ts}`-Output** Add your own `remove = output<void>();{:ts}` for the delete-button.
- **Build the template** Move the input, remove-button and error-`@for{:html}`-Block from `book-create-form.html` into `co-author-input.html`. Bind the input's value and disabled state via `[value]{:html}` and `[disabled]{:html}`, update the value via `(input){:html}`, and emit `touch{:ts}` on `(blur){:html}`. Wire the remove-button's `(click){:html}` to `remove.emit(){:ts}`.

---

- **Use it in `BookCreateForm{:ts}`** Replace the co-author row's markup in `book-create-form.html` with a single `<app-co-author-input [formField]="coAuthor" (remove)="removeCoAuthor(coAuthorIndex)" />{:html}`. Add `CoAuthorInput{:ts}` to the `imports{:ts}`-Array of `BookCreateForm{:ts}`.

Run the application inside the Browser: adding, editing and removing co-authors should work exactly like before — just with much less markup in `BookCreateForm{:ts}`.
