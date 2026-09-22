<details>
<summary>Copy the prepared `BookDetailPage{:ts}`</summary>

```ts
// app.routes.ts
{ path: 'books/detail/:isbn', component: BookDetailPage }
```

</details>

<details>
<summary>Navigate from `BooksPage{:ts}`</summary>

```ts
// books-page.ts
import { Router } from '@angular/router';

private readonly router = inject(Router);

async goToBookDetails(book: Book) {
  await this.router.navigate(['/books', 'detail', book.isbn]);
}
```

</details>

<details>
<summary>Enable Component Input Binding</summary>

```ts
// app.config.ts
import { provideRouter, withComponentInputBinding } from '@angular/router';

provideRouter(routes, withComponentInputBinding());
```

</details>

<details>
<summary>Load the book</summary>

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

</details>
