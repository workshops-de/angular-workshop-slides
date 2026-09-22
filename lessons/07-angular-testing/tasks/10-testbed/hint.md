```ts
// book-card.spec.ts
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { BookCard } from './book-card';
import { Book } from '../book';

describe('BookCard', () => {
  const book: Book = {
    isbn: '978-3-16-148410-0',
    cover: '',
    title: 'Moby Dick',
    author: 'Herman Melville',
    abstract: 'A whale of a tale.'
  };

  let fixture: ComponentFixture<BookCard>;

  beforeEach(() => {
    TestBed.configureTestingModule({});

    fixture = TestBed.createComponent(BookCard);
    fixture.componentRef.setInput('content', book);
    fixture.detectChanges();
  });

  it('should display the book title', () => {
    const title = fixture.nativeElement.querySelector('h3');
    expect(title.textContent).toContain('Moby Dick');
  });

  it('should display the author and abstract', () => {
    const host: HTMLElement = fixture.nativeElement;

    expect(host.querySelector('h4')?.textContent).toContain('Herman Melville');
    expect(host.querySelector('p')?.textContent).toContain('A whale of a tale.');
  });
});
```
