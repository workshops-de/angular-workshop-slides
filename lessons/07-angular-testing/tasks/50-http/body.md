So far you tested **components** through the DOM. The piece that actually talks to the backend — `BooksClient{:ts}` (`src/app/books/books-client.ts`) — deserves its own focused test: no component, no template, just the service and a **fake HTTP backend**. Angular's `provideHttpClientTesting(){:ts}` swaps the real HTTP handler for one that never hits the network — every request is captured and answered by _you_, via **`HttpTestingController{:ts}`**.

- **Create the spec file** `src/app/books/books-client.spec.ts`.

---

- **Write a `describe('BooksClient', ...){:ts}`-block** with a module-level `Book{:ts}` fixture (`mobyDick{:ts}` — reuse the shape from the previous tasks).

---

- Inside a `beforeEach(){:ts}`:
  - `TestBed.configureTestingModule({ providers: [provideHttpClient(), provideHttpClientTesting()] }){:ts}` (import `provideHttpClient{:ts}` from `@angular/common/http`, `provideHttpClientTesting{:ts}` from `@angular/common/http/testing`).
  - `httpMock = TestBed.inject(HttpTestingController);{:ts}`
  - `booksClient = TestBed.inject(BooksClient);{:ts}` — it's `providedIn: 'root'{:ts}`, so no need to list it as a provider.
- Add an `afterEach(() => httpMock.verify());{:ts}` — this fails the test if a request was fired that you never `expectOne{:ts}`'d or `flush{:ts}`'ed.
- **`it('requests a single book by ISBN', ...){:ts}`**:
  - `let actual: Book | undefined;{:ts}` then `booksClient.getByIsbn(mobyDick.isbn).subscribe(book => (actual = book));{:ts}`
  - `httpMock.expectOne(...){:ts}` for `http://localhost:4730/books/<isbn>`, assert method `GET`.
  - `req.flush(mobyDick);{:ts}` — this resolves the Observable synchronously.
  - `expect(actual).toEqual(mobyDick);{:ts}`

---

- **`it('sends a new book via POST', ...){:ts}`**:
  - `const draft: Partial<Book> = { title: 'Clean Code', author: 'Robert C. Martin', isbn: '978-0-13-235088-4', abstract: '', cover: '' };{:ts}`
  - `booksClient.create(draft).subscribe();{:ts}`
  - `const req = httpMock.expectOne('http://localhost:4730/books');{:ts}`
  - `expect(req.request.method).toBe('POST');{:ts}`
  - `expect(req.request.body).toEqual(draft);{:ts}`
  - `req.flush({ ...draft });{:ts}`

---

- **`it('updates a book via PUT', ...){:ts}`**: same pattern for `booksClient.update(mobyDick.isbn, changes){:ts}`, expecting `http://localhost:4730/books/${mobyDick.isbn}`, method `PUT`, body `changes{:ts}`, `flush(changes){:ts}`.

Run `npm test{:bash}`.

> `getAll(){:ts}` returns an `httpResource{:ts}`, not an `Observable{:ts}` — a resource fetches on its own inside an injection context, so it isn't exercised with the `subscribe(){:ts}` + `expectOne(){:ts}` pattern here. It is already covered at component level in `books-page.spec.ts`.
> The `subscribe{:ts}` + captured-variable style works because `flush(){:ts}` delivers the response synchronously. If you prefer `async/await`, `const actual = await lastValueFrom(booksClient.getByIsbn(mobyDick.isbn));{:ts}` right after the `flush(){:ts}` reads just as well.
