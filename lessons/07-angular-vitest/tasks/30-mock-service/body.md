A real unit test isolates the thing under test — every dependency gets mocked or stubbed. `BooksPage` (`src/app/books/books-page.ts`) injects `BooksClient` and exposes its books through `getAll()`, which returns an `httpResource`. The component reads `.value()`, `.isLoading()` and `.error()` off that resource. Let's test `BooksPage` without ever hitting a real (or even mocked) HTTP backend, by mocking `BooksClient` itself with **Vitest's `vi.fn()`**.

- **Create the spec file** `src/app/books/books-page.spec.ts` (there's an existing `books-page.spec.ts` in the solution you can look at for inspiration once you're done, but try it yourself first).
- **Build a resource-shaped mock**: `getAll()` must return a stub carrying the members `BooksPage` reads — `value()`, `isLoading()`, `error()`:
  ```ts
  const booksClientMock: Partial<BooksClient> = {
    getAll: vi.fn().mockReturnValue({
      value: () => [book1, book2],
      isLoading: () => false,
      error: () => undefined
    } as unknown as ReturnType<BooksClient['getAll']>)
  };
  ```
- **Register the mock**: `await render(BooksPage, { providers: [{ provide: BooksClient, useValue: booksClientMock }] });`.
- **Write an `it('renders all books from the mocked BooksClient', ...)`**: assert both book titles are `.toBeInTheDocument()`, and that `booksClientMock.getAll` `.toHaveBeenCalled()`.
- **Write a second `it('filters books by the search term', ...)`**: use `userEvent` to type into the search field — `screen.getByRole('searchbox')` finds it (the `<input type="search">` has an implicit ARIA role) — and assert only the matching book is still visible, while the other one is `.not.toBeInTheDocument()` via `screen.queryByText(...)`.

Run `npm test`.
