## The books list

```ts
// books-page.ts
books = signal<Book[]>([
  {
    id: 'how-to-win-friends',
    title: 'How to win friends',
    author: 'Dale Carnegie',
    publishedAt: new Date('1936-10-01')
  },
  {
    id: 'the-willpower-instinct',
    title: 'The Willpower Instinct: How Self-Control Works ...',
    author: 'Kelly McGonigal',
    publishedAt: new Date('2011-12-29')
  },
  {
    id: 'start-with-why',
    author: 'Simon Sinek',
    title: 'Start with WHY',
    publishedAt: new Date('2009-10-29')
  }
]);
```

## Rendering the list with @for

```html
<!-- books-page.html -->
<div class="book-grid">
  @for (book of books(); track book.id) {
    <app-book-card
      [book]="book"
      (detailClick)="goToBookDetails($event)"
      (deleteClick)="deleteBook($event)"
    />
  }
</div>
```
