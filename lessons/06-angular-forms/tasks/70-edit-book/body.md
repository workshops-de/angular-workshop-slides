Let's reuse everything we learned to build an Edit-Page for an existing book.

- **Copy the prepared `BookEditPage{:ts}`** Copy the folders `book-edit-page` and `book-edit-form` from `workshop-support/books/` into `src/app/books/`.
- **Add the route** Configure a new Route inside `book.routes.ts`, displaying the `BookEditPage{:ts}` (path: `edit/:isbn`), lazy-loaded like the existing `detail/:isbn`-Route.

> The "Edit"-Link on `BookDetailPage{:ts}` already points to this route — nothing to do there.

---

- **Extend `BooksClient{:ts}`** Add an `update(isbn: string, book: Partial<Book>){:ts}`-Method that sends a PUT request to _/books/:isbn_. Add a `getByIsbnResource(isbn: Signal<string>){:ts}`-Method that returns an `httpResource<Book>(){:ts}` for _/books/:isbn_ (with the current `isbn(){:ts}`).
- **Read the route param** Inside `BookEditForm{:ts}`, declare `readonly isbn = input.required<string>();{:ts}` to receive the `:isbn` route param (passed down from `BookEditPage{:ts}`).
- **Load the book** Inject `BooksClient{:ts}` and call `getByIsbnResource(this.isbn){:ts}` — the resource re-fetches whenever `isbn(){:ts}` changes.

---

- **Seed the form's model** Derive a `model{:ts}` with `linkedSignal(){:ts}`: use `bookResource.value{:ts}` as `source{:ts}` and a `computation{:ts}` that maps the loaded book onto the empty form (falling back to the empty values while it's still loading).
- **Build the form** Call `form(){:ts}` with the `model{:ts}` signal and a schema function, reusing `required(){:ts}` and `validAuthorName(){:ts}` from the previous tasks for `title{:ts}` and `author{:ts}`.
  - The `isbn{:ts}` shouldn't be editable: mark it with `readonly(schemaPath.isbn){:ts}` inside the schema function.
  - Disable the whole form while the book is loading: `disabled(schemaPath, { when: () => this.bookResource.isLoading() }){:ts}`.
- **Submit the form** Pass a `submission.action{:ts}` that calls `BooksClient.update(){:ts}` with `isbn(){:ts}` and the current `model(){:ts}`.
- **Build the template** `book-edit-form.html` already has the fields laid out — wire it up like `BookCreateForm{:ts}`: `[formRoot]{:html}`, `[formField]{:html}` per field, and the error-`@for{:html}`-Blocks. Note the ISBN field is `readonly{:ts}` here and there's no co-authors collection in the edit form.

Run the application inside the Browser: Open a book, click "Edit", change a field and save — the change should be persisted on the Backend.
