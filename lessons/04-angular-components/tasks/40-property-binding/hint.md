## Defining a style object

A `[style]`-Binding accepts an object whose keys are CSS properties. Keep the object inside a `signal`.

```ts
import { Component, signal } from '@angular/core';

export class BookCard {
  customStyle = signal({
    color: 'red'
  });
}
```

```html
<!-- book-card.html -->
<h4 [style]="customStyle()">{{ content().author }}</h4>
```
