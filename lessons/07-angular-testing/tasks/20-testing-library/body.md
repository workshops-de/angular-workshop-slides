Testing through `TestBed{:ts}` directly involves a lot of repetitive boilerplate: manual change detection, DOM querying by tag or CSS-selector, and coupling your test to markup details that have nothing to do with what you're actually testing. **Angular Testing Library** (ATL) wraps `TestBed{:ts}` and nudges you towards accessible, user-centric tests instead — "the more your tests resemble the way your software is used, the more confidence they can give you."

`@testing-library/angular`, `@testing-library/user-event` and `@testing-library/jest-dom` are already installed in this project.

---

- **Render with ATL** In _book-card.spec.ts_ replace `TestBed.configureTestingModule{:ts}` + `createComponent{:ts}` + `setInput{:ts}` + `detectChanges{:ts}` with a single `await render(BookCard, { componentInputs: { book }, providers: [BookMarkerStore] }){:ts}` call from `@testing-library/angular`.

---

- **Query like a user** Replace `fixture.nativeElement.querySelector(...){:ts}` with `screen.getByText(...){:ts}` and assert each is `.toBeInTheDocument(){:ts}` — for the title and the author.

---

- **Test the content projection** `BookCard{:ts}` renders whatever the parent projects via `<ng-content />{:html}` (that's how the "Details"-Link ends up inside the card since the content-projection task).
  - Declare a tiny host component with the template `<app-book-card [book]="book">Details</app-book-card>{:html}`.
  - `render(){:ts}` it (again with `providers: [BookMarkerStore]{:ts}`) and assert `screen.getByText('Details'){:ts}` is in the document.

---

- **Run the tests** Run `npm test{:bash}` again — all cases should be green. Compare the two versions side by side — which one reads closer to "what does a user actually see and do"?
