A real unit test isolates the thing under test — every dependency gets mocked or stubbed. `BooksPage{:ts}` (_src/app/books/books-page/books-page.ts_) injects `BooksClient{:ts}` and exposes its books through `getAll(){:ts}`, which returns an `httpResource{:ts}`. The component reads `.value(){:ts}`, `.isLoading(){:ts}` and `.error(){:ts}` off that resource. Let's test `BooksPage{:ts}` without ever hitting a real (or even mocked) HTTP backend, by mocking `BooksClient{:ts}` itself with **Vitest's `vi.fn(){:ts}`**.

---

- **Create the spec file** Create _src/app/books/books-page/books-page.spec.ts_ next to the component.

---

- **Build a resource-shaped mock** `getAll(){:ts}` must return a stub carrying the members `BooksPage{:ts}` reads — `value(){:ts}`, `isLoading(){:ts}`, `error(){:ts}`:

  ```ts
  const booksClientMock: Partial<BooksClient> = {
    getAll: vi.fn().mockReturnValue({
      value: () => [book1, book2],
      isLoading: () => false,
      error: () => undefined
    } as unknown as ReturnType<BooksClient['getAll']>)
  };
  ```

---

- **Reset the search term** `BookMarkerStore{:ts}` stores the search term in `localStorage{:ts}`, so it survives from one test to the next. Add `beforeEach(() => localStorage.clear());{:ts}` to start every test with an empty search.

---

- **Register the mock** Pass it to `render(){:ts}`: `await render(BooksPage, { providers: [{ provide: BooksClient, useValue: booksClientMock }] });{:ts}`.

---

- **Test the rendering** Write an `it('renders all books from the mocked BooksClient', ...){:ts}`: assert both book titles are `.toBeInTheDocument(){:ts}`, and that `booksClientMock.getAll{:ts}` `.toHaveBeenCalled(){:ts}`.

---

- **Test the filter** Write a second `it('filters books by the search term', ...){:ts}`:
  - Use `userEvent{:ts}` to type into the search field — `screen.getByRole('searchbox'){:ts}` finds it (the `<input type="search">{:html}` has an implicit ARIA role).
  - Assert only the matching book is still visible, while the other one is `.not.toBeInTheDocument(){:ts}`.
  - Use `screen.getByRole('heading', { name: mobyDick.title }){:ts}` and `screen.queryByRole('heading', { name: friends.title }){:ts}`. `getByText(){:ts}` doesn't work here: `BookMarker{:ts}` highlights the search term and splits the title into `<mark>Moby</mark> Dick{:html}`. The accessible name of the heading is still the full title.

---

- **Run the tests** Run `npm test{:bash}` — both cases should be green.
