A real unit test isolates the thing under test — every dependency gets mocked or stubbed. `BooksPage{:ts}` (`src/app/books/books-page.ts`) injects `BooksClient{:ts}` and exposes its books through `getAll(){:ts}`, which returns an `httpResource{:ts}`. The component reads `.value(){:ts}`, `.isLoading(){:ts}` and `.error(){:ts}` off that resource. Let's test `BooksPage{:ts}` without ever hitting a real (or even mocked) HTTP backend, by mocking `BooksClient{:ts}` itself with **Vitest's `vi.fn(){:ts}`**.

- **Create the spec file** `src/app/books/books-page.spec.ts` (there's an existing `books-page.spec.ts` in the solution you can look at for inspiration once you're done, but try it yourself first).
- **Build a resource-shaped mock**: `getAll(){:ts}` must return a stub carrying the members `BooksPage{:ts}` reads — `value(){:ts}`, `isLoading(){:ts}`, `error(){:ts}`:
  ```ts
  const booksClientMock: Partial<BooksClient> = {
    getAll: vi.fn().mockReturnValue({
      value: () => [book1, book2],
      isLoading: () => false,
      error: () => undefined
    } as unknown as ReturnType<BooksClient['getAll']>)
  };
  ```
- **Register the mock**: `await render(BooksPage, { providers: [{ provide: BooksClient, useValue: booksClientMock }] });{:ts}`.
- **Write an `it('renders all books from the mocked BooksClient', ...){:ts}`**: assert both book titles are `.toBeInTheDocument(){:ts}`, and that `booksClientMock.getAll{:ts}` `.toHaveBeenCalled(){:ts}`.
- **Write a second `it('filters books by the search term', ...){:ts}`**: use `userEvent{:ts}` to type into the search field — `screen.getByRole('searchbox'){:ts}` finds it (the `<input type="search">{:html}` has an implicit ARIA role) — and assert only the matching book is still visible, while the other one is `.not.toBeInTheDocument(){:ts}` via `screen.queryByText(...){:ts}`.

Run `npm test{:bash}`.
