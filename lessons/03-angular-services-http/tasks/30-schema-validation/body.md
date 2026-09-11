The API is an external system - never trust its payload blindly. [valibot](https://valibot.dev) lets us describe the expected shape once and fail fast when the data drifts.

---

- **Add valibot** Install the dependency: `npm install valibot`.

---

- **Describe the `Book` schema** Open _book.ts_ and replace the hand-written `Book` interface with a `valibot` schema. Model the fields the API returns: `isbn` and `title` as required strings, `author`, `cover`, `subtitle`, `price`, `numPages` as optional, and `publishedAt` as an optional ISO string that is `transform`ed into a `Date`. Export `BooksCollectionSchema` for the array and derive the type via `v.InferOutput`.

---

- **Parse the response** In _books-client.ts_ run the loaded data through `v.parse(BooksCollectionSchema, value)` before it reaches the app, so every consumer receives validated `Book` objects. With `httpResource` this is the `parse` option.

---

- **Check the result** The list still renders. Temporarily rename a required field in the schema and confirm you now get a parse error instead of a silent `undefined`.
