```typescript
// books-client.ts
import { httpResource } from '@angular/common/http';
import { Signal } from '@angular/core';

getByIsbnResource(isbn: Signal<string>) {
  return httpResource<Book>(() => ({ url: `${this.baseUrl}/books/${isbn()}` }));
}

update(isbn: string, book: Partial<Book>): Observable<Book> {
  return this.http.put<Book>(`${this.baseUrl}/books/${isbn}`, book);
}
```

```typescript
// book-edit-page.ts
import { Component, inject, input, linkedSignal } from '@angular/core';
import { disabled, form, FormField, FormRoot, readonly, required } from '@angular/forms/signals';
import { firstValueFrom } from 'rxjs';
import { BooksClient } from '../books-client';
import { validAuthorName } from '../validators/author';

const emptyBookForm = { isbn: '', title: '', subtitle: '', author: '', abstract: '' };

@Component({
  selector: 'app-book-edit',
  imports: [FormField, FormRoot],
  templateUrl: './book-edit-page.html'
})
export class BookEditPage {
  private readonly booksClient = inject(BooksClient);
  protected readonly isbn = input.required<string>();

  private readonly bookResource = this.booksClient.getByIsbnResource(this.isbn);

  protected readonly model = linkedSignal({
    source: this.bookResource.value,
    computation: loadedBook => (loadedBook ? { ...emptyBookForm, ...loadedBook } : emptyBookForm)
  });

  protected readonly form = form(
    this.model,
    schemaPath => {
      readonly(schemaPath.isbn);
      required(schemaPath.title, { message: 'Please insert a title.' });
      required(schemaPath.author, { message: 'Please insert an Author.' });
      validAuthorName(schemaPath.author);
      disabled(schemaPath, { when: () => this.bookResource.isLoading() });
    },
    {
      submission: {
        action: async () => {
          await firstValueFrom(this.booksClient.update(this.isbn(), this.model()));
          return null;
        }
      }
    }
  );
}
```

```html
<!-- book-detail-page.html -->
<a [routerLink]="['/books/edit', book.isbn]">Edit</a>
```
