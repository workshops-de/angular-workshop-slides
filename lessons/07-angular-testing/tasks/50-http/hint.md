```ts
// books-client.spec.ts
import { TestBed } from '@angular/core/testing';
import { provideHttpClient } from '@angular/common/http';
import { HttpTestingController, provideHttpClientTesting } from '@angular/common/http/testing';
import { BooksClient } from './books-client';
import { Book } from './book';

describe('BooksClient', () => {
  const mobyDick: Book = {
    isbn: '978-3-16-148410-0',
    cover: '',
    title: 'Moby Dick',
    author: 'Herman Melville',
    abstract: 'A whale of a tale.'
  };

  let booksClient: BooksClient;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [provideHttpClient(), provideHttpClientTesting()]
    });

    httpMock = TestBed.inject(HttpTestingController);
    booksClient = TestBed.inject(BooksClient);
  });

  afterEach(() => httpMock.verify());

  it('requests a single book by ISBN', () => {
    let actual: Book | undefined;
    booksClient.getByIsbn(mobyDick.isbn).subscribe(book => (actual = book));

    const req = httpMock.expectOne(`http://localhost:4730/books/${mobyDick.isbn}`);
    expect(req.request.method).toBe('GET');

    req.flush(mobyDick);

    expect(actual).toEqual(mobyDick);
  });

  it('sends a new book via POST', () => {
    const draft: Partial<Book> = {
      title: 'Clean Code',
      author: 'Robert C. Martin',
      isbn: '978-0-13-235088-4',
      abstract: '',
      cover: ''
    };

    booksClient.create(draft).subscribe();

    const req = httpMock.expectOne('http://localhost:4730/books');
    expect(req.request.method).toBe('POST');
    expect(req.request.body).toEqual(draft);

    req.flush({ ...draft });
  });

  it('updates a book via PUT', () => {
    const changes: Partial<Book> = { ...mobyDick, title: 'Moby Dick (revised)' };

    booksClient.update(mobyDick.isbn, changes).subscribe();

    const req = httpMock.expectOne(`http://localhost:4730/books/${mobyDick.isbn}`);
    expect(req.request.method).toBe('PUT');
    expect(req.request.body).toEqual(changes);

    req.flush(changes);
  });
});
```

> `getAll()` returns an `httpResource`, not an `Observable` — a resource fetches on its own inside an injection context, so it isn't exercised with the `subscribe()` + `expectOne()` pattern. It is covered at component level in `books-page.spec.ts`.
