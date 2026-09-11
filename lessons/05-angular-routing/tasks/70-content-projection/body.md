We know about routing now. This allows us to embrace its tools to improve our coding even more.
Wouldn't it be nice to have a more declarative way to use navigation in our components?
To inject the Router and to write additional methods feels odd.

Let's use content projection to make our `BookCard` more flexible and to reduce boilerplate code.

Let's replace the fixed "Details"-Link inside the `BookCard` with Content Projection, so the parent decides what gets shown there.

1. **Remove the Output** Inside `book-card.ts` remove the `detailClick`-Output and the `handleDetailClick`-Method - we don't need them anymore.
2. **Add `<ng-content />`** Inside `book-card.html` replace the removed `<a>`-Link with `<ng-content />`.
3. **Project the Link** Inside `books-page.html`, add the "Details"-Link between the opening and closing tag of `<app-book-card>`. Use `[routerLink]="['detail', book.isbn]"` instead of the previous `(click)`-Handler.
4. **Adjust the imports** Inside `books-page.ts` import `RouterLink` from `@angular/router` and add it to the `imports`-Array of the Component. Remove the now unused `Router`, `goToBookDetails` and `Book` import.
