## Assert the error path

A green test for the happy path isn't the whole story. Callers of `BooksClient{:ts}` need to know that a failing request surfaces as an error, not as a silent `undefined{:ts}`.

- **Error from an `Observable{:ts}`** Write an `it('propagates a 500 from POST as an error', ...){:ts}`:
  - Declare `let actual: HttpErrorResponse | undefined;{:ts}`, then subscribe with both callbacks: `booksClient.create(mobyDick).subscribe({ next: () => expect.unreachable('expected an error'), error: (err: HttpErrorResponse) => (actual = err) });{:ts}` (import `HttpErrorResponse{:ts}` from `@angular/common/http`).
  - `httpMock.expectOne('http://localhost:4730/books').flush('Kaboom', { status: 500, statusText: 'Server Error' });{:ts}`
  - Assert `expect(actual?.status).toBe(500);{:ts}` and `expect(actual?.error).toBe('Kaboom');{:ts}`
- **Error from the resource** Write an `it('exposes a failed GET via error()', async () => ...){:ts}`:
  - Create the resource and send the request as in the GET test (`TestBed.runInInjectionContext(...){:ts}`, `TestBed.tick(){:ts}`).
  - Answer it with the same `flush('Kaboom', { status: 500, statusText: 'Server Error' }){:ts}`.
  - `await vi.waitFor(() => expect(booksResource.error()).toBeInstanceOf(HttpErrorResponse));{:ts}`
  - `expect(booksResource.hasValue()).toBe(false);{:ts}` — careful: in the error state, `value(){:ts}` **throws**. Use `hasValue(){:ts}` to check for a value safely.
- **Bonus of the bonus** Simulate a network failure instead of an HTTP status: `req.error(new ProgressEvent('Network error')){:ts}` on the captured POST request, then assert `expect(actual).toBeInstanceOf(HttpErrorResponse);{:ts}` and `expect(actual?.status).toBe(0);{:ts}`.
