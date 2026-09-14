```typescript
// book-new-page.ts
import { applyEach, form, FormField, FormRoot, required } from '@angular/forms/signals';
import { Book } from '../book';

export class BookNewPage {
  protected readonly model = signal({
    isbn: '',
    title: '',
    subtitle: '',
    authors: [''],
    abstract: '',
    cover: ''
  });

  protected readonly form = form(this.model, schemaPath => {
    required(schemaPath.isbn, { message: 'Please insert an ISBN.' });
    required(schemaPath.title, { message: 'Please insert a title.' });
    applyEach(schemaPath.authors, author => {
      required(author, { message: 'Please insert an Author.' });
      validAuthorName(author);
    });
  }, {
    submission: {
      action: async () => {
        // The API only supports a single author per book
        const book: Book = { ...this.model(), author: this.model().authors[0] };
        await firstValueFrom(this.booksClient.create(book));
        return null;
      }
    }
  });

  addAuthor() {
    this.model.update(m => ({ ...m, authors: [...m.authors, ''] }));
  }

  deleteAuthor(authorIndex: number) {
    this.model.update(m => ({ ...m, authors: m.authors.filter((_, i) => i !== authorIndex) }));
  }
}
```

```html
@for (author of form.authors; track $index; let authorIndex = $index) {
  <label>
    <span>Author</span>
    <input [formField]="author" />
    @if (author().touched()) {
      @for (error of author().errors(); track error.kind) {
        <small>{{ error.message }}</small>
      }
    }
  </label>
  <button type="button" (click)="deleteAuthor(authorIndex)">Remove Author</button>
}
<button type="button" (click)="addAuthor()">Add Author</button>
```
