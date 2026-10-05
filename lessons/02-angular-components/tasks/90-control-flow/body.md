We already have a component being capable of rendering a book.
Let's instrument the component to render a whole list.

- **Turn `book{:ts}` into `books{:ts}`** Open _src/app/books/books-page/books-page.ts_, rename the property _book_ to _books_, and change its type from `Book{:ts}` to `Book[]{:ts}`. Wrap your book with an array (`[ ]` / square-brackets) and add at least one additional book to your list. Give every book a unique _id_.
- **Render the list** Switch to the template of _BooksPage_ and use Control Flow `@for{:html}` to render all books of your list, tracking them by `book.id{:ts}`. Keep the output bindings on every `<app-book-card>{:html}` and wrap the cards in a `<div class="book-grid">{:html}`. Have a look at the browser to check the result.
