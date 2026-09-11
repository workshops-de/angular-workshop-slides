## Storing the search term as a signal

```ts
// app.ts
searchTerm = signal('');
```

## Wiring the search input

```html
<!-- app.html -->

<!-- search input, sets the signal directly -->
<input (input)="searchTerm.set($event.target.value)" />
```

## Filtering with `computed`

```ts
// app.ts
import { computed, signal } from '@angular/core';

// filters the books array and checks if the title contains the search term
booksComputed = computed(() => {
  const searchTerm = this.searchTerm().toLowerCase();

  return this.books().filter(book =>
    book.title.toLowerCase().includes(searchTerm)
  );
});
```

```html
<!-- app.html -->

<!-- use the computed signal -->
@for (book of booksComputed(); track book.title) {
<app-book-card ...> ...</app-book-card>
```
