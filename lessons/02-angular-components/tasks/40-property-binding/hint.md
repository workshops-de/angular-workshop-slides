## Defining a style object

A `[style]{:html}`-Binding accepts an object whose keys are CSS properties. Keep the object inside a `signal{:ts}`.

```ts
// book-card.ts
import { Component, signal } from '@angular/core';

export class BookCard {
  customStyle = signal({
    color: 'red'
  });
}
```

```html
<!-- book-card.html -->
<h4 [style]="customStyle()">Herman Melville</h4>
```

---

## Binding the cover image

`[src]{:html}` is a property binding, too. `placeholderCover{:ts}` never changes, so it is a plain `readonly{:ts}` property and not a signal. That is why it is read **without** parentheses, while `customStyle(){:ts}` is called.

```ts
// book-card.ts
export class BookCard {
  customStyle = signal({ color: 'red' });

  readonly placeholderCover = 'book-cover-placeholder.svg';
}
```

```html
<!-- book-card.html -->
<div class="book-card">
  <img [src]="placeholderCover" alt="" class="book-cover" />

  <div class="book-card-body">
    <!-- ... -->
  </div>
</div>
```
