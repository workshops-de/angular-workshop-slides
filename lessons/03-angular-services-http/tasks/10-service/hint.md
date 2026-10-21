## Generate with Angular CLI

```bash
ng generate service books/book-marker-store
```

---

## Holding and persisting the mark term

```ts
// book-marker-store.ts
import { effect, Service, signal } from '@angular/core';

// autoProvided: false — the service is only available where it is provided (BooksPage).
@Service({ autoProvided: false })
export class BookMarkerStore {
  // Initial value comes from a non-reactive, imperative API (localStorage).
  #markTerm = signal(localStorage.getItem('books.markTerm') ?? '');

  markTerm = this.#markTerm.asReadonly();

  constructor() {
    effect(() => {
      localStorage.setItem('books.markTerm', this.markTerm());
    });
  }

  setMarkTerm(markTerm: string) {
    this.#markTerm.set(markTerm);
  }
}
```

---

## Using the service in `BooksPage{:ts}`

The service is provided in the component's `providers{:ts}`. Everything below _BooksPage_, like the directive inside _BookCard_, finds it through dependency injection.

```ts
// books-page.ts
import { Component, computed, inject, signal } from '@angular/core';
import { BookMarkerStore } from '../book-marker-store';

@Component({
  selector: 'app-books-page',
  templateUrl: './books-page.html',
  imports: [BookCard],
  // Local provider: one instance per BooksPage, shared with all BookCards below it.
  providers: [BookMarkerStore]
})
export class BooksPage {
  bookMarkerStore = inject(BookMarkerStore);

  // no searchTerm signal and no constructor/effect anymore

  booksComputed = computed(() => {
    const markTerm = this.bookMarkerStore.markTerm();
    const books = this.books();

    return books.filter(book => bookMatches(book, markTerm));
  });
}
```

```html
<!-- books-page.html -->
<input
  class="search-field"
  type="search"
  placeholder="Search..."
  [value]="bookMarkerStore.markTerm()"
  (input)="bookMarkerStore.setMarkTerm($event.target.value)"
/>
```

---

## Renaming the directive

```ts
// book-marker.ts (formerly marker.ts)
@Directive({ selector: '[appBookMarker]' })
export class BookMarker {
  // ...
}
```

```ts
// book-card.ts
import { BookMarker } from '../book-marker';

@Component({
  selector: 'app-book-card',
  templateUrl: './book-card.html',
  imports: [DatePipe, BookMarker]
})
export class BookCard {}
```

---

## Using the service in `BookMarker{:ts}`

The directive reads the mark term directly from the service. It is not provided again, so the directive receives the instance of _BooksPage_.

```ts
// book-marker.ts
import { Directive, ElementRef, Renderer2, effect, inject, input } from '@angular/core';
import { BookMarkerStore } from './book-marker-store';

@Directive({ selector: '[appBookMarker]' })
export class BookMarker {
  private renderer = inject(Renderer2);
  private host = inject<ElementRef<HTMLElement>>(ElementRef);

  private bookMarkerStore = inject(BookMarkerStore);

  rawText = input.required<string | undefined>();
  // the `markTerm` input is gone

  constructor() {
    effect(() => this.markText(this.rawText(), this.bookMarkerStore.markTerm()));
  }

  // markText(...) stays unchanged
}
```

---

## Cleaning up `BookCard{:ts}`

```ts
// book-card.ts
export class BookCard {
  // the `markTerm` input is gone
}
```

```html
<!-- book-card.html -->
<h3 appBookMarker [rawText]="currentBook.title"></h3>
<h4 [style]="customStyle()" appBookMarker [rawText]="currentBook.author"></h4>
```
