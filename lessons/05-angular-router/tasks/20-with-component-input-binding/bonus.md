Your detail page already shows a _Delete_ button. Let's make it work and bring the user back to the list afterwards.

---

- **Implement `deleteBook(){:ts}`** In _book-detail-page.ts_ inject `Router{:ts}` and add an `async{:ts}` method `deleteBook(){:ts}`:
  - Ask for confirmation with `window.confirm(){:ts}` and stop if the user cancels.
  - Delete the book with `await lastValueFrom(this.booksClient.delete(this.isbn())){:ts}`.
  - Navigate back to the list with `await this.router.navigate(['/books']){:ts}`.

---

- **Wire the button** In _book-detail-page.html_ bind `(click)="deleteBook()"{:html}` to the _Delete_ button. The comment above the button shows the binding.

---

- **Check the result** Open a book, click _Delete_ and confirm. You land on the list and the book is gone.
