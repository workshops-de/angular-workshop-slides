Let's reuse everything we learned to build an Edit-Page for an existing book. The page loads the book and hands it down to the form — the form itself only knows a `book{:ts}`-Input and a `save{:ts}`-Output.

- **Copy the prepared `BookEditPage{:ts}`** Copy the folders `book-edit-page` and `book-edit-form` from `workshop-support/books/` into `src/app/books/`.
- **Add the route** Configure a new Route inside `book.routes.ts`, displaying the `BookEditPage{:ts}` (path: `edit/:isbn`), lazy-loaded like the existing `detail/:isbn`-Route.

> The "Edit"-Link on `BookDetailPage{:ts}` already points to this route — nothing to do there.

---

- **Extend `BooksClient{:ts}`** Add a `getByIsbnResource(isbn: Signal<string>){:ts}`-Method that returns an `httpResource<Book>(){:ts}` for _/books/:isbn_ (with the current `isbn(){:ts}`). The `update(){:ts}`-Method (PUT) already exists from the HTTP lesson.

---

- **Load the book** Inside `BookEditPage{:ts}`:
  - Declare `readonly isbn = input.required<string>();{:ts}` to receive the `:isbn` route param.
  - Inject `BooksClient{:ts}` and call `getByIsbnResource(this.isbn){:ts}` — the resource re-fetches whenever `isbn(){:ts}` changes. Keep it in a `bookResource{:ts}` property.
  - Add a method `saveBook(book: Book){:ts}` that calls `update(){:ts}` on `BooksClient{:ts}` with `book.isbn{:ts}` and the `book{:ts}` and subscribes to it.
- **Render by state** In `book-edit-page.html` show a loading message while `bookResource.isLoading(){:ts}`, the error message if `bookResource.error(){:ts}` is set, and — once `bookResource.value(){:ts}` is available — the form: `<app-book-edit-form [book]="book" (save)="saveBook($event)" />{:html}`. Move the `<div class="app-content">{:html}` with its `<h1>{:html}` out of the page into `book-edit-form.html` (wrapping the `<form>{:html}`, like in `BookCreateForm{:ts}`).

---

- **Declare input and output** Inside `BookEditForm{:ts}` declare `readonly book = input.required<Book>();{:ts}` and `readonly save = output<Book>();{:ts}`.
- **Seed the form's model** Inputs are read-only, so derive a writable copy with `linkedSignal(){:ts}`: spread an `emptyBookForm{:ts}` constant and the `book(){:ts}` into one object. `emptyBookForm{:ts}` holds an empty string for every field of the form (`isbn{:ts}`, `title{:ts}`, `subtitle{:ts}`, `author{:ts}`, `abstract{:ts}` and `cover{:ts}`), because optional `Book{:ts}` properties might be missing, but every form field needs a value to bind to.

---

- **Build the form** Call `form(){:ts}` with the `model{:ts}` signal and a schema function, reusing `required(){:ts}` and `validAuthorName(){:ts}` from the previous tasks for `title{:ts}` and `author{:ts}`.
  - The `isbn{:ts}` shouldn't be editable: mark it with `readonly(schemaPath.isbn){:ts}` inside the schema function.
- **Announce the edited book** Pass a `submission.action{:ts}` that emits the current `model(){:ts}` via `save{:ts}` and returns `null{:ts}`. Sending the book is up to the parent page.

---

- **Build the template** `book-edit-form.html` already has the fields laid out — wire it up like `BookCreateForm{:ts}`: `[formRoot]{:html}`, `[formField]{:html}` per field (the `<textarea>{:html}` for the abstract works the same way as an `<input>{:html}`), the error-`@for{:html}`-Blocks for `title{:ts}` and `author{:ts}`, and the disabled Submit-Button. Remove the old `name{:html}` and `readonly{:html}` attributes. Note there's no co-authors collection in the edit form.
- **Update the cover preview** The prepared form uses temporary logic (`coverUrl{:ts}`, `coverBroken{:ts}`, `coverPreview{:ts}`, `onCoverInput(){:ts}`) for the cover preview. Remove it and let the preview read from the model instead: `[src]="model().cover || placeholderCover"{:html}`. Expose the existing `PLACEHOLDER_COVER{:ts}` constant to the template via a `placeholderCover{:ts}` property.

Run the application inside the Browser: Open a book, click "Edit", change a field and save — the change should be persisted on the Backend. The ISBN field must stay read-only.
