Let's reuse everything we learned to build an Edit-Page for an existing book.

- **Generate `BookEditPage`** Create a new Component `BookEditPage` for the Book-Feature with `ng generate component books/book-edit/book-edit-page`.
- **Add the route** Configure a new Route inside `book.routes.ts`, displaying the `BookEditPage` (path: `edit/:isbn`), lazy-loaded like the existing `detail/:isbn`-Route.
- **Link to it** Add an "Edit"-Link with `routerLink` from `BookDetailPage` to the `edit/:isbn`-Route of the currently displayed book.

---

- **Extend `BooksClient`** Add an `update(isbn: string, book: Partial<Book>)`-Method that sends a PUT request to `` `${baseUrl}/books/${isbn}` ``. Add a `getByIsbnResource(isbn: Signal<string>)`-Method that returns an `httpResource<Book>()` for `` `${baseUrl}/books/${isbn()}` ``.
- **Read the route param** Inside `BookEditPage`, declare `protected readonly isbn = input.required<string>();` to receive the `:isbn` route param.
- **Load the book** Inject `BooksClient` and call `getByIsbnResource(this.isbn)` — the resource re-fetches whenever `isbn()` changes.

---

- **Seed the form's model** Derive a `model` with `linkedSignal()`: use `bookResource.value` as `source` and a `computation` that maps the loaded book onto the empty form (falling back to the empty values while it's still loading).
- **Build the form** Call `form()` with the `model` signal and a schema function, reusing `required()` and `validAuthorName()` from the previous tasks for `title` and `author`.
  - The `isbn` shouldn't be editable: mark it with `readonly(schemaPath.isbn)` inside the schema function.
  - Disable the whole form while the book is loading: `disabled(schemaPath, { when: () => this.bookResource.isLoading() })`.
- **Submit the form** Pass a `submission.action` that calls `BooksClient.update()` with `isbn()` and the current `model()`.
- **Build the template** Reuse the markup from `BookNewPage`'s template — `[formRoot]`, `[formField]` per field, and the error-`@for`-Blocks.

Run the application inside the Browser: Open a book, click "Edit", change a field and save — the change should be persisted on the Backend.
