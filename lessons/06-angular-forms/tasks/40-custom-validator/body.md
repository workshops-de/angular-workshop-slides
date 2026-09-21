- **Create the validator file** Create a folder `books/validators` and add a file `author.ts`.

---

- **Write the validator** Create a function `validAuthorName(schemaPath: SchemaPath<string>): void{:ts}` that calls `validate(){:ts}` from `@angular/forms/signals`, passing in the `schemaPath{:ts}` and a callback `field => { ... }{:ts}`.
  - Inside the callback, read the current value with `field.value(){:ts}` and check if it contains any digits (Hint: you can use a Regex for this: `/[0-9]+/.test(value){:ts}`).
  - If the value contains any digits return a validation error object: `{ kind: 'invalidAuthor', message: 'Name must not contain digits' }{:ts}`, otherwise return `null{:ts}`.

---

- **Wire it up** Call your `validAuthorName(){:ts}`-Function inside the schema function of `BookCreateForm{:ts}`, passing in `schemaPath.author{:ts}`.

> We don't need a specific handling of the error message in the template, because we are using already a `for{:ts}`-loop.
