```ts
// books-page.spec.ts
import { Component, input } from '@angular/core';
import { render, screen } from '@testing-library/angular';
import { BooksPage } from './books-page';
import { BooksClient } from './books-client';
import { Book } from './book';

@Component({
  selector: 'app-book-card',
  template: `<div data-testid="mock-book-card">{{ content().title }}</div>`
})
class BookCardMock {
  content = input.required<Book>();
}

describe('BooksPage', () => {
  const mobyDick: Book = {
    isbn: '978-3-16-148410-0',
    cover: '',
    title: 'Moby Dick',
    author: 'Herman Melville',
    abstract: 'A whale of a tale.'
  };
  const friends: Book = {
    isbn: '978-0-671-72322-5',
    cover: '',
    title: 'How to win friends',
    author: 'Dale Carnegie',
    abstract: 'A self-help classic.'
  };

  function booksClientMock(books: Book[]): Partial<BooksClient> {
    return {
      getAll: vi.fn().mockReturnValue({
        value: () => books,
        isLoading: () => false,
        error: () => undefined
      } as unknown as ReturnType<BooksClient['getAll']>)
    };
  }

  it('renders one book card per book, without depending on BookCard internals', async () => {
    await render(BooksPage, {
      componentImports: [BookCardMock],
      providers: [{ provide: BooksClient, useValue: booksClientMock([mobyDick, friends]) }]
    });

    const cards = screen.getAllByTestId('mock-book-card');
    expect(cards).toHaveLength(2);
    expect(cards[0]).toHaveTextContent('Moby Dick');
    expect(cards[1]).toHaveTextContent('How to win friends');
  });
});
```
