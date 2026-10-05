## Phase 1: Integrate `Sidebar`{:ts}

Add `Sidebar{:ts}` to the `imports{:ts}` array of the `@Component{:ts}` decorator, then use its selector `app-sidebar` in the template. `Sidebar{:ts}` ships ready-to-use from `@workshop-support` — no `ng generate{:bash}` needed.

```ts
// app.ts
import { Component } from '@angular/core';
import { Sidebar } from '@workshop-support';

@Component({
  selector: 'app-root',
  imports: [Sidebar],
  templateUrl: './app.html'
})
export class App {}
```

```html
<!-- app.html -->
<app-sidebar />
<app-welcome>{{ warmWelcome() }}</app-welcome>
```

---

## Phase 2: Build the `BookCard`{:ts} template

Use this static markup in _book-card.html_. The class names match the styles that are already provided, so the card looks right without writing any CSS.

```html
<!-- book-card.html -->
<div class="book-card">
  <div class="book-card-body">
    <h3>Moby Dick</h3>
    <h4>Herman Melville</h4>
    <p class="book-published">1851-10-18</p>
    <div class="book-card-actions">
      <a href="" class="btn-secondary">More</a>
      <button type="button" class="btn-danger">Delete</button>
    </div>
  </div>
</div>
```

---

## Phase 2: Nest `BookCard`{:ts} inside `BooksPage`{:ts}

Add `BookCard{:ts}` to the `imports{:ts}` array of `BooksPage{:ts}`'s `@Component{:ts}` decorator so its selector `app-book-card` becomes available in _books-page.html_.

```ts
// books-page.ts
import { Component } from '@angular/core';

import { BookCard } from '../book-card/book-card';

@Component({
  selector: 'app-books-page',
  imports: [BookCard],
  templateUrl: './books-page.html'
})
export class BooksPage {}
```

```html
<!-- books-page.html -->
<app-book-card />
```

---

## Integrate `BooksPage`{:ts} into _App_

Add `BooksPage{:ts}` to the `imports{:ts}` array in _app.ts_, and replace `<app-welcome>{:html}` with `<app-books-page />{:html}` in _app.html_.

```ts
// app.ts
import { Component } from '@angular/core';
import { Sidebar } from '@workshop-support';

import { BooksPage } from './books/books-page/books-page';

@Component({
  selector: 'app-root',
  imports: [Sidebar, BooksPage],
  templateUrl: './app.html'
})
export class App {}
```

```html
<!-- app.html -->
<app-sidebar />
<app-books-page />
```
