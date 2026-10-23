Angular ships with **Vitest** as its default test runner (since Angular v21) — no extra setup needed for this project. Run the existing test suite once to see it in action:

```bash
npm test
```

You should see one passing test coming from _src/app/app.spec.ts_.

Every 1st-class Angular building block can be **unit tested** in isolation. Let's write a test the "vanilla" way — directly through `TestBed{:ts}` — for `BookCard{:ts}` (_src/app/books/book-card/book-card.ts_). We'll upgrade it to Angular Testing Library in the next task, so keep it plain for now.

---

- **Create the spec file** Create _src/app/books/book-card/book-card.spec.ts_.

---

- **Set up the test** Write a `describe('BookCard', ...){:ts}`-block. Inside a `beforeEach(){:ts}`:
  - Call `TestBed.configureTestingModule({ providers: [BookMarkerStore] }){:ts}`. The `BookMarker{:ts}`-Directive in the card's template injects `BookMarkerStore{:ts}`. In the app, `BooksPage{:ts}` provides it — in the test, you have to.
  - Create the fixture with `TestBed.createComponent(BookCard){:ts}`.
  - Define a small test `Book{:ts}`-object and set it via `fixture.componentRef.setInput('book', book){:ts}` — `book{:ts}` is a `required{:ts}` Input, so it must be set before the first `detectChanges(){:ts}`.
  - Call `fixture.detectChanges(){:ts}`.

---

- **Test the title** Write an `it('should display the book title', ...){:ts}`: query `fixture.nativeElement.querySelector('h3'){:ts}` and assert its `textContent{:ts}` contains your test book's title with `expect(...).toContain(...){:ts}`.

---

- **Test the author** Write a second `it('should display the book author', ...){:ts}`: query the `<h4>{:html}` element and assert its `textContent{:ts}` contains your test book's `author{:ts}`.

---

- **Run the tests** Run `npm test{:bash}` — both cases should turn green.
