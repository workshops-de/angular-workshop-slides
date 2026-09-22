<details>
<summary>Turn `book{:ts}` into `books{:ts}`</summary>

```ts
// app.ts
books = signal<Book[]>([
  {
    title: 'How to win friends',
    author: 'Dale Carnegie',
    abstract: "How to Win Friends and Influence ..."
  },
  {
    title: 'The Willpower Instinct: How Self-Control Works ...',
    author: 'Kelly McGonigal',
    abstract: 'Based on Stanford University ...'
  },
  {
    author: 'Simon Sinek',
    title: 'Start with WHY',
    abstract: "START WITH WHY shows that the leaders who've ..."
  }
]);
```

</details>

<details>
<summary>Render the list</summary>

```html
<!-- app.html -->
@for(book of books(); track book.title){
  <app-book-card ... >
}
```

</details>
