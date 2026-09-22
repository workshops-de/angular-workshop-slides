<details>
<summary>Meet the App component</summary>

A `signal{:ts}` is read by calling it as a function. That's why the template uses `warmWelcome(){:ts}` and not `warmWelcome{:ts}`.

```ts
// app.ts
warmWelcome = signal('Angularian');
```

```html
<!-- app.html -->
<app-welcome>{{ warmWelcome() }}</app-welcome>
```

</details>

<details>
<summary>Add a second signal</summary>

```ts
// app.ts
import { Component, signal } from '@angular/core';

export class App {
  warmWelcome = signal('Angularian');
  greet = signal('Hello');
}
```

</details>

<details>
<summary>Update a signal from a `constructor{:ts}`</summary>

Use `.update(...){:ts}` when the new value depends on the current one. Its callback receives the current value and returns the next one.

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

</details>

<details>
<summary>Check the result</summary>

> Angular tracks which signals a template reads and automatically re-renders it whenever one of them changes — that's what "reactivity" means here.

</details>
