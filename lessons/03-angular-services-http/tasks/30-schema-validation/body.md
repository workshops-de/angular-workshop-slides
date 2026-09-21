The API is an external system - never trust its payload blindly. [valibot](https://valibot.dev) lets us describe the expected shape once and fail fast when the data drifts.

---

- **Add valibot** Install the dependency: `npm install valibot{:bash}`.

---

- **Describe the `Book{:ts}` schema** Open _book.ts_ and replace the hand-written `Book{:ts}` interface with a `valibot` schema. Model the fields the API returns: `isbn{:ts}` and `title{:ts}` as required strings, `author{:ts}`, `cover{:ts}`, `subtitle{:ts}`, `price{:ts}`, `numPages{:ts}` as optional, and `publishedAt{:ts}` as an optional ISO string that is `transform{:ts}`ed into a `Date{:ts}`. Export `BooksCollectionSchema{:ts}` for the array and derive the type via `v.InferOutput{:ts}`.

---

- **Parse the response** In _books-client.ts_ run the loaded data through `v.parse(BooksCollectionSchema, value){:ts}` before it reaches the app, so every consumer receives validated `Book{:ts}` objects. With `httpResource{:ts}` this is the `parse{:ts}` option.

---

- **Check the result** The list still renders. Temporarily rename a required field in the schema and confirm you now get a parse error instead of a silent `undefined{:ts}`.
