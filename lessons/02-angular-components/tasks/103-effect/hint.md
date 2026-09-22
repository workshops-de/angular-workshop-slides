<details>
<summary>Seed the signal from `localStorage{:ts}`</summary>

```ts
// books-page.ts
// Initial value comes from a non-reactive, imperative API (localStorage).
searchTerm = signal(localStorage.getItem('books.searchTerm') ?? '');
```

</details>

<details>
<summary>Persist the search term with `effect{:ts}`</summary>

```ts
// books-page.ts
import { effect } from '@angular/core';

constructor() {
  effect(() => {
    localStorage.setItem('books.searchTerm', this.searchTerm());
  });
}
```

An `effect{:ts}` runs once after it is created and re-runs whenever a signal it reads
(`searchTerm{:ts}`) changes - so every keystroke is written through to `localStorage{:ts}`.

</details>
