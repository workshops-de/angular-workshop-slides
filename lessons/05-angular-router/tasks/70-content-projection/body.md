We know about routing now. This allows us to embrace its tools to improve our coding even more.
Wouldn't it be nice to have a more declarative way to use navigation in our components?
To inject the Router and to write additional methods feels odd.

Let's use content projection to make our `BookCard{:ts}` more flexible and to reduce boilerplate code.

Let's replace the fixed "Details"-Link inside the `BookCard{:ts}` with Content Projection, so the parent decides what gets shown there.

- **Remove the Output** Inside `book-card.ts` remove the `detailClick{:ts}`-Output and the `handleDetailClick{:ts}`-Method - we don't need them anymore.

---

- **Add `<ng-content />{:html}`** Inside `book-card.html` replace the removed `<a>{:html}`-Link with `<ng-content />{:html}`.

---

- **Project the Link** Inside `books-page.html`, add the "Details"-Link between the opening and closing tag of `<app-book-card>{:html}`. Use `[routerLink]="['detail', book.isbn]"{:html}` instead of the previous `(click){:html}`-Handler.

---

- **Adjust the imports** Inside `books-page.ts` import `RouterLink{:ts}` from `@angular/router` and add it to the `imports{:ts}`-Array of the Component. Remove the now unused `Router{:ts}`, `goToBookDetails{:ts}` and `Book{:ts}` import.
