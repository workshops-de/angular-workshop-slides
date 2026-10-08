## Enable Component Input Binding

```ts
// app.config.ts
import { provideRouter, withComponentInputBinding } from '@angular/router';

provideRouter(routes, withComponentInputBinding());
```

## The component

```ts
// book-detail-page.ts
import { Component, inject, input } from '@angular/core';
import { RouterLink } from '@angular/router';

import { BookDetail } from '../book-detail/book-detail';
import { BooksClient } from '../books-client';

@Component({
  selector: 'app-book-detail-page',
  imports: [RouterLink, BookDetail],
  templateUrl: './book-detail-page.html'
})
export class BookDetailPage {
  private booksClient = inject(BooksClient);
  isbn = input('');

  bookResource = this.booksClient.getByIsbn(this.isbn);
}
```

```html
<!-- book-detail-page.html -->
@if (bookResource.value(); as book) {
  <app-book-detail [book]="book" />
}
```

## Extend BooksPage

```ts
// books-page.ts
import { Router } from '@angular/router';

private readonly router = inject(Router);

async goToBookDetails(book: Book) {
  await this.router.navigate(['/books', 'detail', book.isbn]);
}
```

## Extend your routes definitions

```ts
// app.routes.ts
{ path: 'books/detail/:isbn', component: BookDetailPage }
```
