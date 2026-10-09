## Routes

```ts
// app.routes.ts
import { Routes } from '@angular/router';
import { Welcome } from '@workshop-support';
import { BooksPage } from './books/books-page/books-page';
import { BookCreatePage } from './books/book-create-page/book-create-page';

export const routes: Routes = [
  {
    path: '',
    component: Welcome,
    pathMatch: 'full'
  },
  {
    path: 'books',
    component: BooksPage
  },
  {
    path: 'books/create',
    component: BookCreatePage
  }
];
```

```ts
// app.config.ts
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes) /* ... */]
};
```

## Router outlet

```ts
// app.ts
import { RouterOutlet } from '@angular/router';
import { Sidebar } from '@workshop-support';

@Component({
  selector: 'app-root',
  imports: [Sidebar, RouterOutlet],
  templateUrl: './app.html'
})
export class App {}
```

```html
<!-- app.html -->
<div class="app-shell">
  <app-sidebar />
  <main>
    <router-outlet />
  </main>
</div>
```
