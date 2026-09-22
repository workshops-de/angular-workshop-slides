<details>
<summary>Add unsaved-changes state</summary>

```ts
// book-create-page.ts
export class BookCreatePage {
  readonly hasUnsafeChanges = signal(true);
}
```

</details>

<details>
<summary>Create a guard function</summary>

- Import the `CanDeactivateFn{:ts}` interface from `@angular/router`
- Type the guard with the guarded component (`BookCreatePage{:ts}`) and implement the fat arrow function

```ts
// confirm-leave.ts
import { CanDeactivateFn } from '@angular/router';
import { BookCreatePage } from './book-create-page/book-create-page';

export const confirmLeaveGuardFn: CanDeactivateFn<BookCreatePage> = component => {
  if (!component.hasUnsafeChanges()) {
    return true;
  }

  return confirm('You have unsaved changes. Do you really want to leave?');
};
```

</details>

<details>
<summary>Wire up the guard</summary>

Add guard to route:

```ts
// book.routes.ts
{
  path: 'create',
  loadComponent: () => import('./book-create-page/book-create-page').then(c => c.BookCreatePage),
  canDeactivate: [confirmLeaveGuardFn]
}
```

</details>
