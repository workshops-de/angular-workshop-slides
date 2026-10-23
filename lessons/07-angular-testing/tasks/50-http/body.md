So far you tested **components** through the DOM. The piece that actually talks to the backend — `BooksClient{:ts}` (_src/app/books/books-client.ts_) — deserves its own focused test: no component, no template, just the service and a **fake HTTP backend**. Angular's `provideHttpClientTesting(){:ts}` swaps the real HTTP handler for one that never hits the network — every request is captured and answered by _you_, via **`HttpTestingController{:ts}`**.

---

- **Create the spec file** Create _src/app/books/books-client.spec.ts_.

---

- **Write the `describe{:ts}`-block** Write a `describe('BooksClient', ...){:ts}`-block with a `Book{:ts}` fixture `mobyDick{:ts}` (reuse the shape from the previous tasks).

---

- **Set up the testing backend** Inside a `beforeEach(){:ts}`:
  - `TestBed.configureTestingModule({ providers: [provideHttpClient(), provideHttpClientTesting()] }){:ts}` (import `provideHttpClient{:ts}` from `@angular/common/http`, `provideHttpClientTesting{:ts}` from `@angular/common/http/testing`).
  - `httpMock = TestBed.inject(HttpTestingController);{:ts}`
  - `booksClient = TestBed.inject(BooksClient);{:ts}` — `@Service(){:ts}` provides it in the root injector, so there is no need to list it as a provider.
  - Add an `afterEach(() => httpMock.verify());{:ts}` — this fails the test if a request was fired that you never `expectOne{:ts}`'d or `flush{:ts}`'ed.

---

- **Test the GET request** `getAll(){:ts}` returns an `httpResource{:ts}`, not an `Observable{:ts}`. There is nothing to `subscribe(){:ts}` to: a resource fires its request on its own, but only inside an injection context. Write an `it('loads the first 15 books via GET', async () => ...){:ts}`:
  - `const booksResource = TestBed.runInInjectionContext(() => booksClient.getAll());{:ts}` creates the resource in an injection context.
  - `TestBed.tick();{:ts}` lets Angular run its pending work, so the resource actually sends the request.
  - `const req = httpMock.expectOne(r => r.url === 'http://localhost:4730/books');{:ts}` — match by `url{:ts}` only, because the request also carries query params.
  - Assert the params: `expect(req.request.params.get('_start')).toBe('0');{:ts}` and `expect(req.request.params.get('_end')).toBe('15');{:ts}`
  - `req.flush([mobyDick]);{:ts}`
  - The resource updates its `value(){:ts}` asynchronously, so wait for it: `await vi.waitFor(() => expect(booksResource.value()).toEqual([mobyDick]));{:ts}`

---

- **Test the POST request** Write an `it('creates a book via POST', ...){:ts}`. `create(){:ts}` returns an `Observable{:ts}`, so you subscribe and capture the result:
  - `let created: Book | undefined;{:ts}` then `booksClient.create(mobyDick).subscribe(book => (created = book));{:ts}`
  - `const req = httpMock.expectOne('http://localhost:4730/books');{:ts}`
  - `expect(req.request.method).toBe('POST');{:ts}` and `expect(req.request.body).toEqual(mobyDick);{:ts}`
  - `req.flush(mobyDick);{:ts}` — this delivers the response synchronously, so `created{:ts}` is set right away.
  - `expect(created).toEqual(mobyDick);{:ts}`

---

- **Test the PUT request** Write an `it('updates a book via PUT', ...){:ts}` with the same pattern for `booksClient.update(mobyDick.isbn, mobyDick){:ts}`, expecting _http://localhost:4730/books/&lt;isbn&gt;_, method `PUT`, body `mobyDick{:ts}` and the flushed book as result.

---

- **Test the DELETE request** Write an `it('deletes a book via DELETE', ...){:ts}`:
  - `let done = false;{:ts}` then `booksClient.delete(mobyDick.isbn).subscribe(() => (done = true));{:ts}`
  - Expect _http://localhost:4730/books/&lt;isbn&gt;_ with method `DELETE`.
  - `req.flush(null);{:ts}` and `expect(done).toBe(true);{:ts}`

---

- **Run the tests** Run `npm test{:bash}` — all four cases should be green, and `httpMock.verify(){:ts}` must not report open requests.
