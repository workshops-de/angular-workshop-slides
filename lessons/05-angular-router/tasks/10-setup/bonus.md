- **Catch unknown URLs** Add a wildcard route `{ path: '**', redirectTo: '' }{:ts}` as the **last** entry of `routes{:ts}`. Open [localhost:4200/foo](http://localhost:4200/foo): instead of an empty page you land on the start page. Move the wildcard route to the top for a moment: now every URL redirects, because the router takes the first route that matches.

---

- **Show page titles** Give each route a `title{:ts}`, e.g. `title: 'Books'{:ts}`. Navigate through the app and watch the title of the browser tab change.

```ts
// app.routes.ts
export const routes: Routes = [
  { path: '', component: Welcome, pathMatch: 'full', title: 'Welcome' },
  { path: 'books', component: BooksPage, title: 'Books' },
  { path: 'books/create', component: BookCreatePage, title: 'Create Book' },
  { path: '**', redirectTo: '' }
];
```
