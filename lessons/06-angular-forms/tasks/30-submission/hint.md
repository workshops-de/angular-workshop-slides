## Inject the service and wire up the submission

```ts
// book-create-form.ts
import { Component, inject, output, signal } from '@angular/core';
import { form, FormField, FormRoot, required } from '@angular/forms/signals';
import { firstValueFrom } from 'rxjs';
import { BooksClient } from '../books-client';

export class BookCreateForm {
  private readonly booksClient = inject(BooksClient);

  // Tells the page that the book has been saved.
  readonly saved = output<void>();

  protected readonly model = signal({ ... });

  protected readonly form = form(
    this.model,
    schemaPath => {
      required(schemaPath.isbn, { message: 'Please insert an ISBN.' });
      required(schemaPath.title, { message: 'Please insert a title.' });
      required(schemaPath.author, { message: 'Please insert an Author.' });
    },
    {
      submission: {
        action: async () => {
          try {
            await firstValueFrom(this.booksClient.create(this.model()));
            this.saved.emit();
            return null;
          } catch {
            return { kind: 'server', message: 'Failed to create book' };
          }
        }
      }
    }
  );
}
```

---

## Tell the page that the book is saved

```html
<!-- book-create-page.html -->
<app-book-create-form (saved)="hasUnsavedChanges.set(false)" />
```
