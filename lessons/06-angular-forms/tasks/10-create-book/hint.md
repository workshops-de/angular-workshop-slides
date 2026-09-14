## Generate the component

```sh
ng generate component books/book-new/book-new-page
```

## The component class

```typescript
// book-new-page.ts
import { Component, signal } from '@angular/core';
import { form, FormField, FormRoot } from '@angular/forms/signals';

@Component({
  selector: 'app-book-new',
  imports: [FormField, FormRoot],
  templateUrl: './book-new-page.html'
})
export class BookNewPage {
  protected readonly model = signal({
    isbn: '',
    title: '',
    subtitle: '',
    author: '',
    abstract: ''
  });

  protected readonly form = form(this.model);
}
```

## The template

```html
<form [formRoot]="form">
  <label>
    <span>ISBN</span>
    <input [formField]="form.isbn" />
  </label>
  <label>
    <span>Title</span>
    <input [formField]="form.title" />
  </label>
  <label>
    <span>Subtitle</span>
    <input [formField]="form.subtitle" />
  </label>
  <label>
    <span>Author</span>
    <input [formField]="form.author" />
  </label>
  <label>
    <span>Abstract</span>
    <input [formField]="form.abstract" />
  </label>

  <button type="submit" [disabled]="form().invalid()">Save</button>
</form>
```
