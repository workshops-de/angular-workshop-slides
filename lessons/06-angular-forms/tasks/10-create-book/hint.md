## The component class

```typescript
// book-create-form.ts
import { Component, signal } from '@angular/core';
import { form, FormField, FormRoot } from '@angular/forms/signals';

@Component({
  selector: 'app-book-create-form',
  imports: [FormField, FormRoot],
  templateUrl: './book-create-form.html'
})
export class BookCreateForm {
  protected readonly model = signal({
    isbn: '',
    title: '',
    subtitle: '',
    author: '',
    abstract: ''
  });

  protected readonly form = form(this.model, {
    submission: {
      action: formField => {
        console.log(formField().controlValue(), this.model());
        return Promise.resolve(null);
      }
    }
  });
}
```

## The template

```html
<form class="form-fields" [formRoot]="form">
  <label class="field-label">
    <span class="field-label-text">ISBN</span>
    <input class="field-input w-full" [formField]="form.isbn" />
  </label>
  <label class="field-label">
    <span class="field-label-text">Title</span>
    <input class="field-input w-full" [formField]="form.title" />
  </label>
  <label class="field-label">
    <span class="field-label-text">Subtitle</span>
    <input class="field-input w-full" [formField]="form.subtitle" />
  </label>
  <label class="field-label">
    <span class="field-label-text">Author</span>
    <input class="field-input w-full" [formField]="form.author" />
  </label>
  <label class="field-label">
    <span class="field-label-text">Abstract</span>
    <input class="field-input w-full" [formField]="form.abstract" />
  </label>

  <div class="form-actions">
    <button type="submit" class="btn-primary" [disabled]="form().invalid()">Save</button>
  </div>
</form>
```
