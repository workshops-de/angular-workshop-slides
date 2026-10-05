```ts
// books-page.spec.ts
import { render, screen } from '@testing-library/angular';
import userEvent from '@testing-library/user-event';
import { BooksPage } from './books-page';
import { BooksClient } from './books-client';
import { Book } from './book';

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

  // getAll() returns an httpResource; BooksPage reads value()/isLoading()/error() off it.
  function booksClientMock(books: Book[]): Partial<BooksClient> {
    return {
      getAll: vi.fn().mockReturnValue({
        value: () => books,
        isLoading: () => false,
        error: () => undefined
      } as unknown as ReturnType<BooksClient['getAll']>)
    };
  }

  it('renders all books from the mocked BooksClient', async () => {
    const client = booksClientMock([mobyDick, friends]);

    await render(BooksPage, {
      providers: [{ provide: BooksClient, useValue: client }]
    });

    expect(screen.getByText(mobyDick.title)).toBeInTheDocument();
    expect(screen.getByText(friends.title)).toBeInTheDocument();
    expect(client.getAll).toHaveBeenCalled();
  });

  it('filters books by the search term', async () => {
    await render(BooksPage, {
      providers: [{ provide: BooksClient, useValue: booksClientMock([mobyDick, friends]) }]
    });

    const user = userEvent.setup();
    await user.type(screen.getByRole('searchbox'), 'Moby');

    expect(screen.getByText(mobyDick.title)).toBeInTheDocument();
    expect(screen.queryByText(friends.title)).not.toBeInTheDocument();
  });
});
```
