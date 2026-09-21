We can embrace TypeScripts language features to make developing with Angular more comfortable.

- **Create the `Book{:ts}` interface** Execute `ng generate interface books/book{:bash}` to create the interface. Open _src/app/books/book.ts_ and specify the following properties: _title_, _abstract_, _author_ all as `string{:ts}`.

---

- **Annotate `App{:ts}`** Switch to the _App_ component and annotate the property `book{:ts}` with the interface `Book{:ts}`. You might need to import `Book{:ts}` from _'./books/book'_ if your editor misses to import the type automatically.
- **Annotate `BookCard{:ts}`** Switch to the _BookCard_ component and annotate the `input(){:ts}` signal function with the interface `Book{:ts}` by switching to `input.required<Book>(){:ts}`.
- **Verify** Recognize that you now have auto-completion in both TypeScript- & Template-Files.
