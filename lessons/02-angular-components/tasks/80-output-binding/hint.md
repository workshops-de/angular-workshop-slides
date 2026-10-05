## Declaring and emitting the output

```ts
// src/app/books/book-card/book-card.ts

// Output-Binding
readonly detailClick = output<Book>();
readonly deleteClick = output<Book>();

// Emit an event
this.detailClick.emit(this.book());
this.deleteClick.emit(this.book());
```

## Handling the event in BooksPage

```ts
// src/app/books/books-page/books-page.ts

// handling detailClick-Event
goToBookDetails(book: Book) {
  console.log('Navigate to book details, soon...');
  console.table(book);
}

// handling deleteClick-Event
deleteBook(book: Book) {
  console.log('Delete book, soon...');
  console.table(book);
}
```

```html
<!-- books-page.html -->
<app-book-card
  [book]="book()"
  (detailClick)="goToBookDetails($event)"
  (deleteClick)="deleteBook($event)"
/>
```
