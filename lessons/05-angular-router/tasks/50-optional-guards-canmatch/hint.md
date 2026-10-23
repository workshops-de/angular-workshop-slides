## Create the user state

```ts
// src/app/user-state.ts
import { Service, signal } from '@angular/core';

@Service()
export class UserState {
  // Hard-coded for this exercise: switch to `false` to see the guard block the books routes.
  readonly isLoggedIn = signal(true);
}
```

---

## Create the `canMatch{:ts}`-Guard

A `CanMatchFn{:ts}` runs in an injection context, so you can use `inject(){:ts}` directly.

```ts
// src/app/is-user-authenticated.ts
import { inject } from '@angular/core';
import { CanMatchFn } from '@angular/router';

import { UserState } from './user-state';

export const isUserAuthenticatedGuardFn: CanMatchFn = () => {
  const userState = inject(UserState);

  return userState.isLoggedIn();
};
```

```ts
// src/app/app.routes.ts
import { isUserAuthenticatedGuardFn } from './is-user-authenticated';

export const routes: Routes = [
  // ...
  {
    path: 'books',
    loadChildren: () => import('./books/book.routes').then(mod => mod.bookRoutes),
    canMatch: [isUserAuthenticatedGuardFn]
  }
];
```

---

## Add a fallback route

When `canMatch{:ts}` returns `false{:ts}`, the router skips the route and tries the next one. A second route with the same path catches that case. It must come **after** the protected route.

```ts
// src/app/app.routes.ts
import { LoginHint, Welcome } from '@workshop-support';

export const routes: Routes = [
  // ...
  {
    path: 'books',
    loadChildren: () => import('./books/book.routes').then(mod => mod.bookRoutes),
    canMatch: [isUserAuthenticatedGuardFn]
  },
  {
    // canMatch rejected the route above, so the router keeps looking and lands here.
    path: 'books',
    component: LoginHint
  }
];
```
