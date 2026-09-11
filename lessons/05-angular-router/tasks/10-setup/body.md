- **Refactor `App` into `BooksPage`** The book list has outgrown `App`. Generate a dedicated page component with `ng generate component books/books-page` and give it the selector `app-book`.
  - Move the `books` signal, the `searchTerm` signal, `booksComputed`, the `BooksClient` injection and the `goToBookDetails` method from `App` into `BooksPage`.
  - Move the search input and the `@for`-list from `app.html` into `books-page.html`.
  - For now render `BooksPage` once from `app.html` via `<app-book />` (the next steps replace it with the router outlet).

---

- **Generate `AboutPage`** Create a new component `AboutPage` with `ng generate component about/about-page`.

---

- **Define the routes** Add a new file `app.routes.ts` beside `app.config.ts`. Add an exported constant `routes` as array with type `Routes`.
  - Configure the start route, redirecting to `/about`.
  - Configure a book route, displaying the `BooksPage` (path: _books_).
  - Configure an about route, displaying the `AboutPage` (path: _about_).
- **Provide the router** Add Angular's `provideRouter` with the exported *routes* constant of `app.routes.ts` as argument to the `providers`-Array in `app.config.ts`.

---

- **Add the router outlet** Open the template of `App` ( _app.html_). Replace its content with `router-outlet`. To activate the `router-outlet` you have to import the `RouterOutlet`-Directive in `imports` of the component declaration.
- **Verify** You can test the navigation already by typing the different URLs in the browser.

---

- **Generate `Navigation`** Add a simple `Navigation` component (`ng generate component navigation`), containing 2 links
  - Books
  - About
- **Wire it up** Add the `Navigation` component at your desired place. Use the directive `routerLink` for the 2 links to navigate between the views (also do not forget the import of the `RouterLink`-Directive).

> Don't forget to remove `<app-book>` from `App`'s template, otherwise you will see it twice.
