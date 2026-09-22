<details>
<summary>Prepare `create{:ts}`, `update{:ts}` and `delete{:ts}` methods</summary>

```ts
// books-client.ts
import { HttpClient, httpResource } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';

export class BooksClient {
  private readonly http = inject(HttpClient);
  readonly #baseUrl = 'http://localhost:4730';

  // getAll() { ... httpResource ... }

  create(book: Partial<Book>): Observable<Book> {
    return this.http.post<Book>(`${this.#baseUrl}/books`, book);
  }

  update(isbn: string, book: Partial<Book>): Observable<Book> {
    return this.http.put<Book>(`${this.#baseUrl}/books/${isbn}`, book);
  }

  delete(isbn: string): Observable<void> {
    return this.http.delete<void>(`${this.#baseUrl}/books/${isbn}`);
  }
}
```

</details>

<details>
<summary>Wire the delete action</summary>

```ts
// books-page.ts
import { lastValueFrom } from 'rxjs';

async deleteBook(book: Book) {
  if (!window.confirm(`Delete "${book.title}"?`)) {
    return;
  }

  await lastValueFrom(this.booksClient.delete(book.isbn));
  this.booksResource.reload();
}
```

</details>
