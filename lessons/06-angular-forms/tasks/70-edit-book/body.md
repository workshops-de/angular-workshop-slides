Let's reuse everything we learned to build an Edit-Page for an existing book. The page loads the book and hands it down to the form — the form itself only knows a `book{:ts}`-Input and a `save{:ts}`-Output.

---

- **Copy the prepared `BookEditPage{:ts}`** Copy the folders _book-edit-page_ and _book-edit-form_ from _workshop-support/books/_ into _src/app/books/_.

---

- **Add the route** In _book.routes.ts_ configure a new route with the path _edit/:isbn_ that displays `BookEditPage{:ts}`, lazy-loaded like the existing _detail/:isbn_ route.

---

- **Wire the Edit link** Now that the route exists, open _book-detail-page.html_ and add `[routerLink]="['/books', 'edit', isbn()]"{:html}` to the _Edit_ link. The comment above the link shows the binding.

---

- **Extend `BooksClient{:ts}`** Add a method `getByIsbnResource(isbn: Signal<string>){:ts}` that returns an `httpResource<Book>(){:ts}` for _/books/:isbn_ (with the current `isbn(){:ts}`). The `update(){:ts}`-Method (PUT) already exists from the HTTP lesson.

---

- **Load the book** In _book-edit-page.ts_:
  - Declare `readonly isbn = input.required<string>();{:ts}` to receive the _:isbn_ route param.
  - Inject `BooksClient{:ts}` and call `getByIsbnResource(this.isbn){:ts}` — the resource re-fetches whenever `isbn(){:ts}` changes. Keep it in a `bookResource{:ts}` property.
  - Add a method `saveBook(book: Book){:ts}` that calls `update(){:ts}` on `BooksClient{:ts}` with `book.isbn{:ts}` and the `book{:ts}` and subscribes to it.

---

- **Render by state** In _book-edit-page.html_:
  - Show a loading message while `bookResource.isLoading(){:ts}` and the error message if `bookResource.error(){:ts}` is set.
  - Once `bookResource.value(){:ts}` is available, show the form: `<app-book-edit-form [book]="book" (save)="saveBook($event)" />{:html}`.
  - Move the `<div class="app-content">{:html}` with its `<h1>{:html}` out of the page into _book-edit-form.html_ (wrapping the `<form>{:html}`, like in `BookCreateForm{:ts}`).

---

- **Declare input and output** In _book-edit-form.ts_ declare `readonly book = input.required<Book>();{:ts}` and `readonly save = output<Book>();{:ts}`.

---

- **Seed the form's model** Inputs are read-only, so derive a writable copy with `linkedSignal(){:ts}`: spread an `emptyBookForm{:ts}` constant and the `book(){:ts}` into one object. `emptyBookForm{:ts}` holds an empty string for every field of the form (`isbn{:ts}`, `title{:ts}`, `subtitle{:ts}`, `author{:ts}`, `abstract{:ts}` and `cover{:ts}`), because optional `Book{:ts}` properties might be missing, but every form field needs a value to bind to.

---

- **Build the form** Call `form(){:ts}` with the `model{:ts}` signal and a schema function:
  - Reuse `required(){:ts}` and `validAuthorName(){:ts}` from the previous tasks for `title{:ts}` and `author{:ts}`.
  - The `isbn{:ts}` shouldn't be editable: mark it with `readonly(schemaPath.isbn){:ts}` inside the schema function.

---

- **Announce the edited book** Pass a `submission.action{:ts}` that emits the current `model(){:ts}` via `save{:ts}` and returns `null{:ts}`. Sending the book is up to the parent page.

---

- **Build the template** _book-edit-form.html_ already has the fields laid out. Wire it up like `BookCreateForm{:ts}`:
  - `[formRoot]{:html}` on the `<form>{:html}` and `[formField]{:html}` per field (the `<textarea>{:html}` for the abstract works the same way as an `<input>{:html}`).
  - The error-`@for{:html}`-Blocks for `title{:ts}` and `author{:ts}`, and the disabled Save-Button.
  - Remove the old `name{:html}` and `readonly{:html}` attributes. There is no co-authors collection in the edit form.

---

- **Update the cover preview** The prepared form uses temporary logic (`coverUrl{:ts}`, `coverBroken{:ts}`, `coverPreview{:ts}`, `onCoverInput(){:ts}`) for the cover preview. Remove it and let the preview read from the model instead: `[src]="model().cover || placeholderCover"{:html}`. Expose the existing `PLACEHOLDER_COVER{:ts}` constant to the template via a `placeholderCover{:ts}` property.

---

- **Check the result** Open a book, click _Edit_, change a field and save — the change is persisted on the Backend. The ISBN field stays read-only.
