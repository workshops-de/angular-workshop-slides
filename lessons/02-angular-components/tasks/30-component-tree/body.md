3, 2, 1 Go! You will build your first component tree — in two phases. First you integrate a component that already exists, then you create two new components yourself and nest them into each other.

---

## Phase 1: Integrate an existing Component

- **Import `Sidebar{:ts}`** Open _src/app/app.ts_ and import `Sidebar{:ts}` from `@workshop-support`. Add it to the `imports{:ts}` array of the `@Component{:ts}` decorator.

---

- **Use it in the template** Switch to _src/app/app.html_ and wrap the existing content in a `<div class="app-shell">{:html}`. Place `<app-sidebar class="contents" />{:html}` as its first child and move `<app-welcome>{:html}` into a `<main class="app-content">{:html}` next to it. `Sidebar{:ts}` is already fully built — integrating it is just import, register, and use its selector. No generation needed.

---

- **Check the result** Open [localhost:4200](http://localhost:4200). The sidebar should now be visible.

---

## Phase 2: Create new Components and integrate them

- **Generate `BooksPage{:ts}`** Open a second terminal, switch to the directory where your Angular project is located, and execute `ng generate component books/books-page{:bash}`. This component will host your book overview.

---

- **Generate `BookCard{:ts}`** Execute `ng generate component books/book-card{:bash}`. Recognize that two files are generated and that your component (_book-card.ts_) has the selector `app-book-card{:html}`.

---

- **Build a static template** Open _src/app/books/book-card/book-card.html_ and set up a simple HTML template visualizing book-information by using **static data**.
  - title
  - author
  - published date
  - a _More_ link (`<a>{:html}`) to the book details
  - a _Delete_ button (`<button>{:html}`)

  The link and the button do nothing yet. In later tasks you will react to their clicks.

  ```html
  <!-- book-card.html -->

  <h3>Moby Dick</h3>
  <h4>Herman Melville</h4>
  <p>1851-10-18</p>

  <!--
  ... More link and Delete button ...
  -->
  ```

---

- **Nest `BookCard{:ts}` inside `BooksPage{:ts}`** Add the missing import for `BookCard{:ts}` to the `imports{:ts}` array in _books-page.ts_, and use `<app-book-card />{:html}` in _books-page.html_.

---

- **Integrate `BooksPage{:ts}` in _App_** Replace `<app-welcome>{:html}` in _app.html_ with `<app-books-page />{:html}`. Add the missing import for `BooksPage{:ts}` to the `imports{:ts}` array in _app.ts_.

---

- **Check the result** Open [localhost:4200](http://localhost:4200). Your full component tree — _App_ containing _Sidebar_ and _BooksPage_, with _BooksPage_ containing _BookCard_ — is displayed in the browser.
