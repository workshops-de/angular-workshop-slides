<details>
<summary>Generate `CoAuthorInput`</summary>

```typescript
// co-author-input.ts
import { Component, input, model, output } from '@angular/core';
import { FormValueControl, ValidationError } from '@angular/forms/signals';

@Component({
  selector: 'app-co-author-input',
  templateUrl: './co-author-input.html'
})
export class CoAuthorInput implements FormValueControl<string> {
  value = model('');

  touched = input(false);
  touch = output<void>();
  disabled = input(false);
  invalid = input(false);
  errors = input<readonly ValidationError[]>([]);

  remove = output<void>();
}
```

</details>

<details>
<summary>Build the template</summary>

```html
<!-- co-author-input.html -->
<div class="field-collection-row">
  <input
    class="field-input min-w-0 flex-1"
    [value]="value()"
    [disabled]="disabled()"
    (input)="value.set($any($event.target).value)"
    (blur)="touch.emit()"
    placeholder="Co-author name"
  />
  <button type="button" class="btn-icon-danger" (click)="remove.emit()" aria-label="Remove co-author">
    ✕
  </button>
</div>
@if (touched()) {
  @for (error of errors(); track error.kind) {
    <small class="field-error">{{ error.message }}</small>
  }
}
```

</details>

<details>
<summary>Use it in `BookCreateForm`</summary>

```html
<!-- book-create-form.html -->
@for (coAuthor of form.coAuthors; track $index; let coAuthorIndex = $index) {
  <app-co-author-input [formField]="coAuthor" (remove)="removeCoAuthor(coAuthorIndex)" />
} @empty {
  <p class="field-hint">No co-authors yet.</p>
}
```

```typescript
// book-create-form.ts
import { CoAuthorInput } from '../co-author-input/co-author-input';

@Component({
  selector: 'app-book-create-form',
  imports: [FormField, FormRoot, CoAuthorInput],
  templateUrl: './book-create-form.html'
})
export class BookCreateForm { /* ... */ }
```

</details>
