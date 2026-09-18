- **Copy the prepared `BookCreatePage`** Copy the folders `book-create-page` and `book-create-form` from `workshop-support/books/` into `src/app/books/`. The copied templates are non-functional for now (a plain `<form>`, an empty component) — you'll wire them up with Signal Forms in the next lesson.

---

- **Define the routes** Add a new file `app.routes.ts` beside `app.config.ts`. Add an exported constant `routes` as array with type `Routes`.
  - Configure the start route (path: `''`, `pathMatch: 'full'`), displaying `Welcome` (imported from `@workshop-support`).
  - Configure a books route, displaying the `BooksPage` (path: `books`).
  - Configure a books-create route, displaying the `BookCreatePage` you just copied (path: `books/create`).

---

- **Provide the router** Add Angular's `provideRouter` with the exported `routes` constant of `app.routes.ts` as argument to the `providers`-Array in `app.config.ts`.

---

- **Add the router outlet** Open the template of `App` (_app.html_). Replace `<app-books-page />` with `<router-outlet />`. Adjust the `imports`-Array of `App` accordingly (remove `BooksPage`, add `RouterOutlet`).
- **Verify** You can test the navigation already by typing the different URLs in the browser.

---

- **Wire up the navigation** `App` already renders a `Sidebar` from `@workshop-support` with 3 placeholder links (Home, Books, New Book). Open `src/app/workshop-support/shell/sidebar/sidebar.html` and add `routerLink`/`routerLinkActive` to each link: `/`, `/books` and `/books/create`.

> Don't forget: the `BookCreatePage` you copied doesn't do anything functional yet — that's expected, its Signal Forms wiring is the topic of the next lesson.
