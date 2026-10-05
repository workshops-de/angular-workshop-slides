## Declaring and emitting the output

```ts
// src/app/books/book-card/book-card.ts

// Output-Binding
readonly detailClick = output<Book>();

// Emit an event
this.detailClick.emit(this.content());
```

## Handling the event in BooksPage

```ts
// src/app/books/books-page/books-page.ts

// handling detailClick-Event
goToBookDetails(book: Book) {
  console.log('Navigate to book details, soon...');
  console.table(book);
}
```
