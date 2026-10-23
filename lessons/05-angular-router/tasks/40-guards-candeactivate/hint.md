## Unsaved-changes state

```ts
// book-create-page.ts
import { Component, signal } from '@angular/core';

export class BookCreatePage {
  readonly hasUnsavedChanges = signal(true);
}
```

---

## Generate the guard

```bash
ng generate guard books/confirm-leave --implements CanDeactivate --skip-tests
```

---

## Implement the guard

The CLI already created the signature. `CanDeactivateFn<unknown>{:ts}` means the guard does not know the component type in advance, so `instanceof{:ts}` checks it at runtime. Inside the `if{:ts}`, TypeScript knows that `component{:ts}` is a `BookCreatePage{:ts}`.

```ts
// confirm-leave-guard.ts
import { CanDeactivateFn } from '@angular/router';

import { BookCreatePage } from './book-create-page/book-create-page';

export const confirmLeaveGuard: CanDeactivateFn<unknown> = (
  component,
  currentRoute,
  currentState,
  nextState
) => {
  if (component instanceof BookCreatePage && component.hasUnsavedChanges()) {
    return confirm('You have unsaved changes. Do you really want to leave?');
  }

  return true;
};
```

---

## Wire up the guard

```ts
// book.routes.ts
import { confirmLeaveGuard } from './confirm-leave-guard';

export const bookRoutes: Routes = [
  // ...
  {
    path: 'create',
    loadComponent: () => import('./book-create-page/book-create-page').then(c => c.BookCreatePage),
    canDeactivate: [confirmLeaveGuard]
  }
];
```
