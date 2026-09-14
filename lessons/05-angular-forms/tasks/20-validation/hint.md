```typescript
// book-new-page.ts
import { form, FormField, FormRoot, required } from '@angular/forms/signals';

protected readonly model = signal({
  isbn: '',
  title: '',
  subtitle: '',
  author: '',
  abstract: ''
});

protected readonly form = form(this.model, schemaPath => {
  required(schemaPath.isbn, { message: 'Please insert an ISBN.' });
  required(schemaPath.title, { message: 'Please insert a title.' });
  required(schemaPath.author, { message: 'Please insert an Author.' });
});
```

```html
<form [formRoot]="form">
  <label>
    <span>Title</span>
    <input [formField]="form.title" />
    @if (form.title().touched()) {
      @for (error of form.title().errors(); track error.kind) {
        <small>{{ error.message }}</small>
      }
    }
  </label>
  <label>
    <span>Author</span>
    <input [formField]="form.author" />
    @if (form.author().touched()) {
      @for (error of form.author().errors(); track error.kind) {
        <small>{{ error.message }}</small>
      }
    }
  </label>
  ....
  <button type="submit" [disabled]="form().invalid()">Save</button>
</form>
```
