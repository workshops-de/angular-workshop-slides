We can embrace TypeScripts language features to make developing with Angular more comfortable.

- **Create the `Book{:ts}` interface** Execute `ng generate interface books/book{:bash}` to create the interface. Open _src/app/books/book.ts_ and specify the following properties: _id_, _title_, _author_ as `string{:ts}` and _publishedAt_ as `Date{:ts}`.

---

- **Annotate `BooksPage{:ts}`** Switch to the _BooksPage_ component and annotate the property `book{:ts}` with the interface `Book{:ts}`. You might need to import `Book{:ts}` from _'./books/book'_ if your editor misses to import the type automatically.
- **Annotate `BookCard{:ts}`** Switch to the _BookCard_ component and annotate the `input(){:ts}` signal function with the interface `Book{:ts}` by switching to `input.required<Book>(){:ts}`. Add an _id_ to your book in _BooksPage_ to satisfy the interface.
- **Verify** Recognize that you now have auto-completion in both TypeScript- & Template-Files.
