Angular ships with **Vitest** as its default test runner (since Angular v21) — no extra setup needed for this project. Run the existing test suite once to see it in action:

```sh
npm test
```

You should see one passing test coming from `books-page.spec.ts`.

---

Every 1st-class Angular building block can be **unit tested** in isolation. Let's write a test the "vanilla" way — directly through `TestBed{:ts}` — for `BookCard{:ts}` (`src/app/books/book-card/book-card.ts`). We'll upgrade it to Angular Testing Library in the next task, so keep it plain for now.

- **Create the spec file** `src/app/books/book-card/book-card.spec.ts`.
- **Write a `describe('BookCard', ...){:ts}`-block**. Inside a `beforeEach(){:ts}`:
  - Call `TestBed.configureTestingModule({}){:ts}`.
  - Create the fixture with `TestBed.createComponent(BookCard){:ts}`.
  - Define a small test `Book{:ts}`-object and set it via `fixture.componentRef.setInput('content', book){:ts}` — `content{:ts}` is a `required{:ts}` Input, so it must be set before the first `detectChanges(){:ts}`.
  - Call `fixture.detectChanges(){:ts}`.
- **Write an `it('should display the book title', ...){:ts}`**: query `fixture.nativeElement.querySelector('h3'){:ts}` and assert its `textContent{:ts}` contains your test book's title with `expect(...).toContain(...){:ts}`.
- **Write a second `it('should display the author and abstract', ...){:ts}`**: query the `<h4>{:html}` and `<p>{:html}` elements and assert their `textContent{:ts}` contains your test book's `author{:ts}` / `abstract{:ts}`.

Run `npm test{:bash}` — both cases should turn green.
