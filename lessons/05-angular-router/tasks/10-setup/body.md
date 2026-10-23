- **Copy the prepared `BookCreatePage{:ts}`** Copy the folders _book-create-page_ and _book-create-form_ from _workshop-support/books/_ into _src/app/books/_. The copied templates are non-functional for now (a plain `<form>{:html}`, an empty component) — you'll wire them up with Signal Forms in the next lesson.

---

- **Define the routes** Add a new file _app.routes.ts_ beside _app.config.ts_. Add an exported constant `routes{:ts}` as array with type `Routes{:ts}`.
  - Configure the start route (path: `''{:ts}`, `pathMatch: 'full'{:ts}`), displaying `Welcome{:ts}` (imported from `@workshop-support`).
  - Configure a books route, displaying the `BooksPage{:ts}` (path: `books{:ts}`).
  - Configure a books-create route, displaying the `BookCreatePage{:ts}` you just copied (path: _books/create_).

---

- **Provide the router** Add Angular's `provideRouter{:ts}` with the exported `routes{:ts}` constant of _app.routes.ts_ as argument to the `providers{:ts}`-Array in _app.config.ts_.

---

- **Add the router outlet** Open the template of `App{:ts}` (_app.html_). Replace `<app-books-page />{:html}` with `<router-outlet />{:html}`. Adjust the `imports{:ts}`-Array of `App{:ts}` accordingly (remove `BooksPage{:ts}`, add `RouterOutlet{:ts}`).

> Don't forget: the `BookCreatePage{:ts}` you copied doesn't do anything functional yet — that's expected, its Signal Forms wiring is the topic of the next lesson.

---

- **Check the result** You can test the navigation already by typing the different URLs in the browser or by clicking the links in the sidebar (they are already wired up).
