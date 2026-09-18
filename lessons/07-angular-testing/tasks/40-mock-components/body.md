`BooksPage` doesn't just depend on a service — it also depends on the `BookCard`-Component to render every list item. Right now, your `BooksPage` tests implicitly also render `BookCard`'s real template. Let's isolate `BooksPage` fully by swapping `BookCard` for a mock component, using `render()`'s `componentImports`-shortcut.

- **Create a mock component** above your `describe`-block: `@Component({ selector: 'app-book-card', template: '<div data-testid="mock-book-card">{{ content().title }}</div>' })`, with `class BookCardMock { content = input.required<Book>(); }` — note the selector must match `BookCard`'s selector exactly (`app-book-card`) so it slots into the same place in `BooksPage`'s template.
- **Swap it in**: `await render(BooksPage, { componentImports: [BookCardMock], providers: [...] });`.
- **Write an `it('renders one book card per book, without depending on BookCard internals', ...)`**:
  - Mock `BooksClient.getAll()` to return a resource-shaped stub with two books (like in the previous task).
  - Query all rendered mock cards with `screen.getAllByTestId('mock-book-card')` and assert `.toHaveLength(2)`.
  - Assert the text content of each card with `.toHaveTextContent(...)`.

A quick note on `getByTestId`: it's the **last resort** in the query priority list (role → label text → placeholder text → text → test id) — it carries no meaning for a real user. Using it here is fine, because we're asserting the *structure* of an intentionally fake component, not real user-facing content.

Run `npm test`.
