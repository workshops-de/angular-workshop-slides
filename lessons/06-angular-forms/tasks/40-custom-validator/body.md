The built-in validators don't cover every rule. An author's name must not contain digits — let's write our own validator for that.

---

- **Create the validator file** Create a folder _books/validators_ and add a file _author.ts_.

---

- **Write the validator** Create a function `validAuthorName(schemaPath: SchemaPath<string>): void{:ts}` that calls `validate(){:ts}` from `@angular/forms/signals`, passing in the `schemaPath{:ts}` and a callback `field => { ... }{:ts}`.
  - Inside the callback, read the current value with `field.value(){:ts}`.
  - Empty values are already covered by `required(){:ts}`, so return `null{:ts}` right away if there is no value.
  - Check if the value contains any digits (hint: use a regular expression, `/[0-9]+/.test(value){:ts}`).
  - If it does, return a validation error object `{ kind: 'invalidAuthor', message: 'Name must not contain digits' }{:ts}`, otherwise return `null{:ts}`.

---

- **Wire it up** In _book-create-form.ts_ call `validAuthorName(schemaPath.author){:ts}` inside the schema function of `BookCreateForm{:ts}`.

> The template needs no change: the `@for{:html}`-Block from the validation task already shows every error message of the field.

---

- **Check the result** Type a name with a digit into the author field and leave it. The message _Name must not contain digits_ appears.
