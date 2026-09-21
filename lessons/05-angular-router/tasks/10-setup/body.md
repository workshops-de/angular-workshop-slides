- **Copy the prepared `BookCreatePage{:ts}`** Copy the folders `book-create-page` and `book-create-form` from `workshop-support/books/` into `src/app/books/`. The copied templates are non-functional for now (a plain `<form>{:html}`, an empty component) — you'll wire them up with Signal Forms in the next lesson.

---

- **Define the routes** Add a new file `app.routes.ts` beside `app.config.ts`. Add an exported constant `routes{:ts}` as array with type `Routes{:ts}`.
  - Configure the start route (path: `''{:ts}`, `pathMatch: 'full'{:ts}`), displaying `Welcome{:ts}` (imported from `@workshop-support`).
  - Configure a books route, displaying the `BooksPage{:ts}` (path: `books{:ts}`).
  - Configure a books-create route, displaying the `BookCreatePage{:ts}` you just copied (path: `books/create`).

---

- **Provide the router** Add Angular's `provideRouter{:ts}` with the exported `routes{:ts}` constant of `app.routes.ts` as argument to the `providers{:ts}`-Array in `app.config.ts`.

---

- **Add the router outlet** Open the template of `App{:ts}` (_app.html_). Replace `<app-books-page />{:html}` with `<router-outlet />{:html}`. Adjust the `imports{:ts}`-Array of `App{:ts}` accordingly (remove `BooksPage{:ts}`, add `RouterOutlet{:ts}`).
- **Verify** You can test the navigation already by typing the different URLs in the browser.

---

- **Wire up the navigation** `App{:ts}` already renders a `Sidebar{:ts}` from `@workshop-support` with 3 placeholder links (Home, Books, New Book). Open `src/app/workshop-support/shell/sidebar/sidebar.html` and add `routerLink{:ts}`/`routerLinkActive{:ts}` to each link: `/`, `/books` and `/books/create`.

> Don't forget: the `BookCreatePage{:ts}` you copied doesn't do anything functional yet — that's expected, its Signal Forms wiring is the topic of the next lesson.
