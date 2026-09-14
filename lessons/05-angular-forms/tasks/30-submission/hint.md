```typescript
// books-client.ts
create(book: Partial<Book>): Observable<Book> {
  return this.http.post<Book>('http://localhost:4730/books', book);
}
```

```typescript
// book-new-page.ts
import { Component, inject, signal } from '@angular/core';
import { form, FormField, FormRoot, required } from '@angular/forms/signals';
import { firstValueFrom } from 'rxjs';
import { BooksClient } from '../books-client';

export class BookNewPage {
  private readonly booksClient = inject(BooksClient);

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
