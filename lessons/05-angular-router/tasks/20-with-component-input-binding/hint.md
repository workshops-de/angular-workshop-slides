## Enable Component Input Binding

```ts
// app.config.ts
import { provideRouter, withComponentInputBinding } from '@angular/router';

provideRouter(routes, withComponentInputBinding());
```

## The component

```ts
// book-detail-page.ts
import { httpResource } from '@angular/common/http';
import { Component, computed, input } from '@angular/core';
import { RouterLink } from '@angular/router';

import { Book } from '../book';
import { BookDetail } from '../book-detail/book-detail';

@Component({
  selector: 'app-book-detail-page',
  imports: [RouterLink, BookDetail],
  templateUrl: './book-detail-page.html'
})
export class BookDetailPage {
  readonly isbn = input('');

  private readonly bookResource = httpResource<Book>(
    () => `http://localhost:4730/books/${this.isbn()}`
  );

  protected readonly book = computed(() => this.bookResource.value());
}
```

```html
<!-- book-detail-page.html -->
@if (book(); as book) {
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
