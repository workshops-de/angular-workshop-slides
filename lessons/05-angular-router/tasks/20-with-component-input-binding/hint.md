## Implement the component

```ts
// book-detail-page.ts

import { ActivatedRoute } from '@angular/router';
import { Observable, switchMap } from 'rxjs';

private readonly route = inject(ActivatedRoute);
private readonly booksClient = inject(BooksClient);

book$: Observable<Book>;

constructor() {
  this.book$ = this.route.params.pipe(
    switchMap(params => this.booksClient.getByIsbn(params?.['isbn']))
  );
}
```

## Extend BooksPage

```ts
// books-page.ts

private readonly router = inject(Router);

goToBookDetails(book: Book) {
  this.router.navigate(['books', 'detail', book.isbn]);
}
```

## Extend your routes definitions

```ts
// app.routes.ts

{ path: 'books/detail/:isbn', component: BookDetailPage }
```

## Extend and use the client with a getByIsbn(isbn: string)

```
HTTP GET http://localhost:4730/books/:isbn
```
