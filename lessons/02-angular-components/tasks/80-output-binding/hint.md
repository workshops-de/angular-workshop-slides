<details>
<summary>Add an output signal</summary>

```ts
// src/app/books/book-card/book-card.ts

// Output-Binding
readonly detailClick = output<Book>();
```

</details>

<details>
<summary>Emit the event</summary>

```ts
// Emit an event
this.detailClick.emit(this.content());
```

</details>

<details>
<summary>Implement the handler</summary>

```ts
// src/app/app.ts

// handling detailClick-Event
goToBookDetails(book: Book) {
  console.log('Navigate to book details, soon...');
  console.table(book);
}
```

</details>
