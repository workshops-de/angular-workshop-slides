Angular ships with **Vitest** as its default test runner (since Angular v21) — no extra setup needed for this project. Run the existing test suite once to see it in action:

```sh
npm test
```

You should see one passing test coming from `books-page.spec.ts`.

---

Every 1st-class Angular building block can be **unit tested** in isolation. Let's write a test the "vanilla" way — directly through `TestBed` — for `BookCard` (`src/app/books/book-card/book-card.ts`). We'll upgrade it to Angular Testing Library in the next task, so keep it plain for now.

- **Create the spec file** `src/app/books/book-card/book-card.spec.ts`.
- **Write a `describe('BookCard', ...)`-block**. Inside a `beforeEach()`:
  - Call `TestBed.configureTestingModule({})`.
  - Create the fixture with `TestBed.createComponent(BookCard)`.
  - Define a small test `Book`-object and set it via `fixture.componentRef.setInput('content', book)` — `content` is a `required` Input, so it must be set before the first `detectChanges()`.
  - Call `fixture.detectChanges()`.
- **Write an `it('should display the book title', ...)`**: query `fixture.nativeElement.querySelector('h3')` and assert its `textContent` contains your test book's title with `expect(...).toContain(...)`.
- **Write a second `it('should display the author and abstract', ...)`**: query the `<h4>` and `<p>` elements and assert their `textContent` contains your test book's `author` / `abstract`.

Run `npm test` — both cases should turn green.
