## app.routes.ts

```ts
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

## books/book.routes.ts

```ts
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

## Lazy load a single component

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
