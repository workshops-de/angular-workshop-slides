## Assert the error path

A green test for the happy path isn't the whole story — callers of `BooksClient` need to know a failing request surfaces as an error, not as a silent `undefined`.

- **Write `it('propagates a 500 as an error', ...)`**:
  - Subscribe with both callbacks: `booksClient.getAll().subscribe({ next: () => fail('expected an error'), error: err => (actual = err) });`
  - `httpMock.expectOne('http://localhost:4730/books').flush('Kaboom', { status: 500, statusText: 'Server Error' });`
  - The `error` callback receives an `HttpErrorResponse` — assert `expect(actual.status).toBe(500);` and `expect(actual.error).toBe('Kaboom');` (import `HttpErrorResponse` from `@angular/common/http` for the type).
- **Bonus of the bonus** — network failure instead of an HTTP status: `.error(new ProgressEvent('Network error'))` on the captured request, then assert `actual instanceof HttpErrorResponse` with `actual.status === 0`.
