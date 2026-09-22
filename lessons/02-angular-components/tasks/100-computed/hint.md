<details>
<summary>The Book filter control</summary>

```ts
// app.ts
searchTerm = signal('');
```

```html
<!-- app.html -->

<!-- search input, sets the signal directly -->
<input (input)="searchTerm.set($event.target.value)" />
```

</details>

<details>
<summary>Derive the filtered books with `computed{:ts}`</summary>

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

</details>

<details>
<summary>Use `booksComputed{:ts}` in the template</summary>

```html
<!-- app.html -->

<!-- use the computed signal -->
@for (book of booksComputed(); track book.title) {
<app-book-card ...> ...</app-book-card>
```

</details>
