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
import { bookMatches } from '@workshop-support';

// filters the books array using the pre-defined helper `bookMatches`
booksComputed = computed(() => {
  const searchTerm = this.searchTerm();
  const books = this.books();

  return books.filter(book => bookMatches(book, searchTerm));
});
```

```html
<!-- app.html -->

<!-- use the computed signal -->
@for (book of booksComputed(); track book.title) {
<app-book-card ...> ...</app-book-card>
```
