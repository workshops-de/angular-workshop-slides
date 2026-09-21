## Assert the error path

A green test for the happy path isn't the whole story — callers of `BooksClient{:ts}` need to know a failing request surfaces as an error, not as a silent `undefined{:ts}`.

- **Write `it('propagates a 500 as an error', ...){:ts}`**:
  - Subscribe with both callbacks: `booksClient.getAll().subscribe({ next: () => fail('expected an error'), error: err => (actual = err) });{:ts}`
  - `httpMock.expectOne('http://localhost:4730/books').flush('Kaboom', { status: 500, statusText: 'Server Error' });{:ts}`
  - The `error{:ts}` callback receives an `HttpErrorResponse{:ts}` — assert `expect(actual.status).toBe(500);{:ts}` and `expect(actual.error).toBe('Kaboom');{:ts}` (import `HttpErrorResponse{:ts}` from `@angular/common/http` for the type).
- **Bonus of the bonus** — network failure instead of an HTTP status: `.error(new ProgressEvent('Network error')){:ts}` on the captured request, then assert `actual instanceof HttpErrorResponse{:ts}` with `actual.status === 0{:ts}`.
