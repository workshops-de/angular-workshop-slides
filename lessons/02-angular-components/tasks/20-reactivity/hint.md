## Reading a signal

A `signal` is read by calling it as a function. That's why the template uses `warmWelcome()` and not `warmWelcome`.

```ts
// app.ts
warmWelcome = signal('Angularian');
```

```html
<!-- app.html -->
<app-welcome>{{ warmWelcome() }}</app-welcome>
```

## Adding the `greet` signal

```ts
// app.ts
import { Component, signal } from '@angular/core';

export class App {
  warmWelcome = signal('Angularian');
  greet = signal('Hello');
}
```

## Updating a signal from the `constructor`

Use `.update(...)` when the new value depends on the current one. Its callback receives the current value and returns the next one.

```ts
// app.ts
export class App {
  warmWelcome = signal('Angularian');
  greet = signal('Hello');

  constructor() {
    setTimeout(() => {
      this.warmWelcome.update(warmWelcome => `${this.greet()} ${warmWelcome}`);
    }, 6000);
  }
}
```

> Angular tracks which signals a template reads and automatically re-renders it whenever one of them changes — that's what "reactivity" means here.
