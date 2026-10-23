Your guard only works for `BookCreatePage{:ts}`. The edit page will need the same protection later. Let's make the guard work for **every** component that offers `hasUnsavedChanges(){:ts}`.

---

- **Describe the contract** Create an interface `HasUnsavedChanges{:ts}` with a single method `hasUnsavedChanges(): boolean{:ts}`.

---

- **Check for the contract** Write a small function `hasUnsavedChangesCheck(component: unknown): component is HasUnsavedChanges{:ts}`. It returns `true{:ts}` if `component{:ts}` is an object and `'hasUnsavedChanges' in component{:ts}` holds.

---

- **Make the guard generic** In `confirmLeaveGuard{:ts}` replace `component instanceof BookCreatePage{:ts}` with your check. The guard no longer imports `BookCreatePage{:ts}` and works for every page with unsaved changes.

---

- **Check the result** The create page still asks before you leave. Pages without `hasUnsavedChanges(){:ts}` can be left right away.

```ts
// confirm-leave-guard.ts
import { CanDeactivateFn } from '@angular/router';

export interface HasUnsavedChanges {
  hasUnsavedChanges(): boolean;
}

function hasUnsavedChangesCheck(component: unknown): component is HasUnsavedChanges {
  return typeof component === 'object' && component !== null && 'hasUnsavedChanges' in component;
}

export const confirmLeaveGuard: CanDeactivateFn<unknown> = component => {
  if (hasUnsavedChangesCheck(component) && component.hasUnsavedChanges()) {
    return confirm('You have unsaved changes. Do you really want to leave?');
  }

  return true;
};
```
