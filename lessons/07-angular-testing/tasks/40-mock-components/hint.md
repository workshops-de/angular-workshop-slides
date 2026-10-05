```ts
// books-page.spec.ts
import { Component, input } from '@angular/core';
import { render, screen } from '@testing-library/angular';
import { BooksPage } from './books-page';
import { BooksClient } from './books-client';
import { Book } from './book';

@Component({
  selector: 'app-book-card',
  template: `<div data-testid="mock-book-card">{{ book().title }}</div>`
})
class BookCardMock {
  book = input.required<Book>();
}

describe('BooksPage', () => {
  const mobyDick: Book = {
    id: 'a1b76e0a-6f19-4c9c-9d3e-1b7f5e2a1c7c',
    isbn: '978-3-16-148410-0',
    cover: '',
    title: 'Moby Dick',
    author: 'Herman Melville'
  };
  const friends: Book = {
    id: '6f0c1c3e-2a41-4f55-9b0e-3d1d7a9e8b52',
    isbn: '978-0-671-72322-5',
    cover: '',
    title: 'How to win friends',
    author: 'Dale Carnegie'
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
