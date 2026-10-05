## Providing the book data

```ts
// books-page.ts
export class BooksPage {
  book = signal({
    title: 'How to win friends',
    author: 'Dale Carnegie',
    abstract: 'In this book ...'
  });
}
```

## Reading an input signal in the template

Input signals are functions — call them with `()` to read their value.

```html
<!-- book-card.html -->
<h3>{{ content().title }}</h3>
<!-- ... -->
```
