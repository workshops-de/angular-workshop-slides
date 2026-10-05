## Storing the search term as a signal

```ts
// books-page.ts
searchTerm = signal('');
```

## Wiring the search input

```html
<!-- books-page.html -->

<!-- search input, sets the signal directly -->
<input
  class="search-field"
  type="search"
  placeholder="Search..."
  (input)="searchTerm.set($event.target.value)"
/>
```

## Filtering with `computed{:ts}`

```ts
// books-page.ts
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
<!-- books-page.html -->

<!-- use the computed signal -->
@for (book of booksComputed(); track book.id) {
  <app-book-card [book]="book" ... />
}
```
