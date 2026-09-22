<details>
<summary>Create the child routes file</summary>

```ts
// app.routes.ts
export const routes: Routes = [
  {
    path: '',
    component: Welcome,
    pathMatch: 'full'
  },
  {
    path: 'books',
    loadChildren: () => import('./books/book.routes').then(module => module.bookRoutes)
  }
];
```

```ts
// books/book.routes.ts
export const bookRoutes: Routes = [
  {
    path: '',
    component: BooksPage
  },
  {
    path: 'create',
    component: BookCreatePage
  },
  {
    path: 'detail/:isbn',
    component: BookDetailPage
  }
];
```

</details>

<details>
<summary>Lazy load the book details route</summary>

```ts
{
  path: 'create',
  loadComponent: () => import('./book-create-page/book-create-page').then(c => c.BookCreatePage)
},
{
  path: 'detail/:isbn',
  loadComponent: () => import('./book-detail-page/book-detail-page').then(c => c.BookDetailPage)
}
```

</details>
