## Seeding the signal from localStorage

```ts
// books-page.ts
// Initial value comes from a non-reactive, imperative API (localStorage).
searchTerm = signal(localStorage.getItem('books.searchTerm') ?? '');
```

--- 

## Persisting with an effect

```ts
// books-page.ts
import { effect } from '@angular/core';

constructor() {
  effect(() => {
    localStorage.setItem('books.searchTerm', this.searchTerm());
  });
}
```

An `effect` runs once after it is created and re-runs whenever a signal it reads
(`searchTerm`) changes - so every keystroke is written through to `localStorage`.
