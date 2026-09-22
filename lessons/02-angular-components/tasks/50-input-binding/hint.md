<details>
<summary>Add an input signal</summary>

Input signals are functions — call them with `()` to read their value.

```html
<!-- book-card.html -->
<h3>{{ content().title }}</h3>
<!-- ... -->
```

</details>

<details>
<summary>Provide a book to bind</summary>

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

</details>
