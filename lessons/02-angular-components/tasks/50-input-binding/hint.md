## Providing the book data

```ts
// app.ts
export class App {
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
