## app.routes.ts

```ts
export const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    redirectTo: '/about'
  },
  {
    path: 'books',
    loadChildren: () => import('./books/book.routes').then(module => module.bookRoutes)
  },
  {
    path: 'about',
    component: AboutPage
  }
];
```

## books/book.routes.ts

```ts
export const bookRoutes: Routes = [
  {
    path: '',
    component: BooksPage
  },
  {
    path: 'detail/:isbn',
    component: BookDetailPage
  }
];
```

## Lazy load a single component

```ts
{
    path: 'detail/:isbn',
    loadComponent: () =>
      import('./book-detail/book-detail-page').then(c => c.BookDetailPage)
 }
```
