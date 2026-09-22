<details>
<summary>Start the API</summary>

If not already installed

```bash
# run bookmonkey-api directly
npx bookmonkey-api@latest
```

</details>

<details>
<summary>Provide the HttpClient</summary>

```typescript
// app.config.ts
import { provideHttpClient } from '@angular/common/http';

providers: [provideHttpClient()];
```

</details>

<details>
<summary>Extend the `Book{:ts}` interface</summary>

```typescript
// book.ts
export interface Book {
  isbn: string;
  title: string;
  subtitle?: string;
  author?: string;
  price?: number;
  numPages?: number;
  cover?: string;
  publishedAt?: string | null;
}
```

</details>

<details>
<summary>Load data via `httpResource{:ts}`</summary>

```typescript
// books-client.ts
import { httpResource } from '@angular/common/http';
import { Service } from '@angular/core';
import { Book } from './book';

@Service()
export class BooksClient {
  readonly #baseUrl = 'http://localhost:4730';

  getAll() {
    return httpResource<Book[]>(
      () => ({
        url: `${this.#baseUrl}/books`,
        params: {
          _start: 0,
          _end: 15,
          _sort: 'createdAt',
          _order: 'desc'
        }
      }),
      { defaultValue: [] }
    );
  }
}
```

</details>

<details>
<summary>Consume the resource in `BooksPage{:ts}`</summary>

```typescript
// books-page.ts
booksResource = this.booksClient.getAll();

booksComputed = computed(() => {
  const searchTerm = this.searchTerm();
  const books = this.booksResource.value();

  return books.filter(book => bookMatches(book, searchTerm));
});
```

</details>

<details>
<summary>Show loading and error state</summary>

```html
<!-- books-page.html -->
@if (booksResource.isLoading()) {
<p>Loading books...</p>
} @else if (booksResource.error(); as error) {
<p>Error: {{ error.message }}</p>
}
```

</details>

<details>
<summary>Show the real cover</summary>

```html
<!-- book-card.html -->
<img [src]="currentBook.cover || placeholderCover" alt="" class="book-cover" />
```

</details>
