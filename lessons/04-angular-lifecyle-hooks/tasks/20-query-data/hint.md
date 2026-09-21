## API starten

If not already installed

```bash
# run bookmonkey-api directly
npx bookmonkey-api
```

---

## Providing HttpClient

```typescript
// app.config.ts
import { provideHttpClient } from '@angular/common/http';

providers: [provideHttpClient()];
```

---

## Extending `Book`

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

---

## Loading books via `httpResource`

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

---

## Consuming the resource in `BooksPage`

```typescript
// books-page.ts
booksResource = this.booksClient.getAll();

booksComputed = computed(() => {
  const searchTerm = this.searchTerm();
  const books = this.booksResource.value();

  return books.filter(book => bookMatches(book, searchTerm));
});
```

---

## Loading and error state

```html
<!-- books-page.html -->
@if (booksResource.isLoading()) {
<p>Loading books...</p>
} @else if (booksResource.error(); as error) {
<p>Error: {{ error.message }}</p>
}
```

---

## Showing the real cover

```html
<!-- book-card.html -->
<img [src]="currentBook.cover || placeholderCover" alt="" class="book-cover" />
```
