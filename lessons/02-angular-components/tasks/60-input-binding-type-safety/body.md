We can embrace TypeScripts language features to make developing with Angular more comfortable.

- **Create the `Book` interface** Execute `ng generate interface books/book` to create the interface. Open _src/app/books/book.ts_ and specify the following properties: _title_, _abstract_, _author_ all as `string`.

---

- **Annotate `App`** Switch to the _App_ component and annotate the property `book` with the interface `Book`. You might need to import `Book` from _'./books/book'_ if your editor misses to import the type automatically.
- **Annotate `BookCard`** Switch to the _BookCard_ component and annotate the `input()` signal function with the interface `Book` by switching to `input.required<Book>()`.
- **Verify** Recognize that you now have auto-completion in both TypeScript- & Template-Files.
