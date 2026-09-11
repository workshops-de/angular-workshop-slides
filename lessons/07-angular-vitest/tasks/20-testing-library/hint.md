```ts
// book-card.spec.ts
import { Component } from '@angular/core';
import { render, screen } from '@testing-library/angular';
import { BookCard } from './book-card';
import { Book } from '../book';

const book: Book = {
  isbn: '978-3-16-148410-0',
  cover: '',
  title: 'Moby Dick',
  author: 'Herman Melville',
  abstract: 'A whale of a tale.'
};

describe('BookCard', () => {
  it('displays the book data passed via the content input', async () => {
    await render(BookCard, { componentInputs: { content: book } });

    expect(screen.getByText(book.title)).toBeInTheDocument();
    expect(screen.getByText('Herman Melville')).toBeInTheDocument();
    expect(screen.getByText(book.abstract)).toBeInTheDocument();
  });

  it('projects content placed between its tags', async () => {
    @Component({
      imports: [BookCard],
      template: `<app-book-card [content]="book">Details</app-book-card>`
    })
    class HostComponent {
      book = book;
    }

    await render(HostComponent);

    expect(screen.getByText('Details')).toBeInTheDocument();
  });
});
```
