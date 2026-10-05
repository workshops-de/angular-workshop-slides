## Providing the book data

```ts
// books-page.ts
export class BooksPage {
  book = signal({
    title: 'How to win friends',
    author: 'Dale Carnegie',
    publishedAt: new Date('1936-10-01')
  });
}
```

```html
<!-- books-page.html -->
<app-book-card [book]="book()" />
```

## Reading an input signal in the template

Input signals are functions — call them with `()` to read their value. A `@let{:html}` variable keeps the template short.

```ts
// book-card.ts
readonly book = input<any>();
```

```html
<!-- book-card.html -->
@let currentBook = book();

<h3>{{ currentBook.title }}</h3>
<h4>{{ currentBook.author }}</h4>
<p class="book-published">{{ currentBook.publishedAt.toLocaleDateString() }}</p>
```
