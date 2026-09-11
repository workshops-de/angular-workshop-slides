So far you tested **components** through the DOM. The piece that actually talks to the backend — `BooksClient` (`src/app/books/books-client.ts`) — deserves its own focused test: no component, no template, just the service and a **fake HTTP backend**. Angular's `provideHttpClientTesting()` swaps the real HTTP handler for one that never hits the network — every request is captured and answered by _you_, via **`HttpTestingController`**.

- **Create the spec file** `src/app/books/books-client.spec.ts`.

---

- **Write a `describe('BooksClient', ...)`-block** with a module-level `Book` fixture (`mobyDick` — reuse the shape from the previous tasks).

---

- Inside a `beforeEach()`:
  - `TestBed.configureTestingModule({ providers: [provideHttpClient(), provideHttpClientTesting()] })` (import `provideHttpClient` from `@angular/common/http`, `provideHttpClientTesting` from `@angular/common/http/testing`).
  - `httpMock = TestBed.inject(HttpTestingController);`
  - `booksClient = TestBed.inject(BooksClient);` — it's `providedIn: 'root'`, so no need to list it as a provider.
- Add an `afterEach(() => httpMock.verify());` — this fails the test if a request was fired that you never `expectOne`'d or `flush`'ed.
- **`it('requests a single book by ISBN', ...)`**:
  - `let actual: Book | undefined;` then `booksClient.getByIsbn(mobyDick.isbn).subscribe(book => (actual = book));`
  - `httpMock.expectOne(...)` for `http://localhost:4730/books/<isbn>`, assert method `GET`.
  - `req.flush(mobyDick);` — this resolves the Observable synchronously.
  - `expect(actual).toEqual(mobyDick);`

---

- **`it('sends a new book via POST', ...)`**:
  - `const draft: Partial<Book> = { title: 'Clean Code', author: 'Robert C. Martin', isbn: '978-0-13-235088-4', abstract: '', cover: '' };`
  - `booksClient.create(draft).subscribe();`
  - `const req = httpMock.expectOne('http://localhost:4730/books');`
  - `expect(req.request.method).toBe('POST');`
  - `expect(req.request.body).toEqual(draft);`
  - `req.flush({ ...draft });`

---

- **`it('updates a book via PUT', ...)`**: same pattern for `booksClient.update(mobyDick.isbn, changes)`, expecting `http://localhost:4730/books/${mobyDick.isbn}`, method `PUT`, body `changes`, `flush(changes)`.

Run `npm test`.

> `getAll()` returns an `httpResource`, not an `Observable` — a resource fetches on its own inside an injection context, so it isn't exercised with the `subscribe()` + `expectOne()` pattern here. It is already covered at component level in `books-page.spec.ts`.
> The `subscribe` + captured-variable style works because `flush()` delivers the response synchronously. If you prefer `async/await`, `const actual = await lastValueFrom(booksClient.getByIsbn(mobyDick.isbn));` right after the `flush()` reads just as well.
