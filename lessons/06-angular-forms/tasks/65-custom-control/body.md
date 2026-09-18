The markup for a single co-author row (input, remove-button, error-list) is starting to clutter `book-create-form.html`. Signal Forms let you extract it into its own component by implementing `FormValueControl` — then `[formField]` can bind to it just like to a plain `<input>`.

- **Generate `CoAuthorInput`** Create a new Component with `ng generate component books/co-author-input`.
- **Implement `FormValueControl<string>`** Add `implements FormValueControl<string>` (from `@angular/forms/signals`) to the class. It requires:
  - `value = model('');` — the two-way bound value.
  - `touched = input(false);`, `disabled = input(false);`, `invalid = input(false);`, `errors = input<readonly ValidationError[]>([]);`
  - `touch = output<void>();` — emitted whenever the control is blurred.
- **Add a `remove`-Output** Add your own `remove = output<void>();` for the delete-button.
- **Build the template** Move the input, remove-button and error-`@for`-Block from `book-create-form.html` into `co-author-input.html`. Bind the input's value to `[value]`, update it via `(input)`, and emit `touch` on `(blur)`. Wire the remove-button's `(click)` to `remove.emit()`.

---

- **Use it in `BookCreateForm`** Replace the co-author row's markup in `book-create-form.html` with a single `<app-co-author-input [formField]="coAuthor" (remove)="removeCoAuthor(coAuthorIndex)" />`. Add `CoAuthorInput` to the `imports`-Array of `BookCreateForm`.

Run the application inside the Browser: adding, editing and removing co-authors should work exactly like before — just with much less markup in `BookCreateForm`.
