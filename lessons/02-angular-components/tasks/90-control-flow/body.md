We already have a component being capable of rendering a book.
Let's instrument the component to render a whole list.

- **Turn `book` into `books`** Open _src/app/app.ts_, rename the property _book_ to _books_, and change its type from `Book` to `Book[]`. Wrap your book with an array (`[ ]` / square-brackets) and add at least one additional book to your list.
- **Render the list** Switch to the template of _App_ and use Control Flow `@for` to render all books of your list. Have a look at the browser to check the result.
