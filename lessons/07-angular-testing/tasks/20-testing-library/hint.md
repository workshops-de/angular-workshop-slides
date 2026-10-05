```ts
// book-card.spec.ts
import { Component } from '@angular/core';
import { render, screen } from '@testing-library/angular';
import { BookCard } from './book-card';
import { Book } from '../book';

const book: Book = {
  id: 'a1b76e0a-6f19-4c9c-9d3e-1b7f5e2a1c7c',
  isbn: '978-3-16-148410-0',
  cover: '',
  title: 'Moby Dick',
  author: 'Herman Melville'
};

describe('BookCard', () => {
  it('displays the book data passed via the book input', async () => {
    await render(BookCard, { componentInputs: { book } });

    expect(screen.getByText(book.title)).toBeInTheDocument();
    expect(screen.getByText(book.author!)).toBeInTheDocument();
  });

  it('projects content placed between its tags', async () => {
    @Component({
      imports: [BookCard],
      template: `<app-book-card [book]="book">Details</app-book-card>`
    })
    class HostComponent {
      book = book;
    }

    await render(HostComponent);

    expect(screen.getByText('Details')).toBeInTheDocument();
  });
});
```
