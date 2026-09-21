`BooksPage{:ts}` doesn't just depend on a service — it also depends on the `BookCard{:ts}`-Component to render every list item. Right now, your `BooksPage{:ts}` tests implicitly also render `BookCard{:ts}`'s real template. Let's isolate `BooksPage{:ts}` fully by swapping `BookCard{:ts}` for a mock component, using `render(){:ts}`'s `componentImports{:ts}`-shortcut.

- **Create a mock component** above your `describe{:ts}`-block: `@Component({ selector: 'app-book-card', template: '<div data-testid="mock-book-card">{{ content().title }}</div>' }){:ts}`, with `class BookCardMock { content = input.required<Book>(); }{:ts}` — note the selector must match `BookCard{:ts}`'s selector exactly (`app-book-card`) so it slots into the same place in `BooksPage{:ts}`'s template.
- **Swap it in**: `await render(BooksPage, { componentImports: [BookCardMock], providers: [...] });{:ts}`.
- **Write an `it('renders one book card per book, without depending on BookCard internals', ...){:ts}`**:
  - Mock `BooksClient.getAll(){:ts}` to return a resource-shaped stub with two books (like in the previous task).
  - Query all rendered mock cards with `screen.getAllByTestId('mock-book-card'){:ts}` and assert `.toHaveLength(2){:ts}`.
  - Assert the text content of each card with `.toHaveTextContent(...){:ts}`.

A quick note on `getByTestId{:ts}`: it's the **last resort** in the query priority list (role → label text → placeholder text → text → test id) — it carries no meaning for a real user. Using it here is fine, because we're asserting the *structure* of an intentionally fake component, not real user-facing content.

Run `npm test{:bash}`.
