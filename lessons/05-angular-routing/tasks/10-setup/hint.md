## Navigation

```html
<ul>
  <li><a routerLink="/books">Books</a></li>
  <li><a routerLink="/about">About</a></li>
</ul>
```

## Routes

```ts
// app.routes.ts
export const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    redirectTo: '/about'
  },
  {
    path: 'books',
    component: BooksPage
  },
  {
    path: 'about',
    component: AboutPage
  }
];
```

```ts
// app.config.ts
// ...
import { provideRouter } from '@angular/router';
// ...

export const appConfig: ApplicationConfig = {
  providers: [provideHttpClient(), provideRouter(routes)]
};
```

## Router outlet and router link

```ts
// app.ts
@Component({
  selector: 'app-root',
  // ...
  imports: [RouterOutlet],
  // ...
})
export class App {}
```

```html
<router-outlet />
```
