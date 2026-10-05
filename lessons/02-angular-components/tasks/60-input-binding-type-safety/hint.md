## Typing the input signal

`input.required<Book>(){:ts}` removes the `undefined{:ts}` case entirely — the signal always resolves to a `Book{:ts}`.

```ts
// book.ts
export interface Book {
  id: string;
  title: string;
  author: string;
  publishedAt: Date;
}

// books-page.ts
book = signal<Book>({
  id: 'how-to-win-friends',
  title: 'How to win friends',
  author: 'Dale Carnegie',
  publishedAt: new Date('1936-10-01')
});

// book-card.ts
readonly book = input.required<Book>();
```
