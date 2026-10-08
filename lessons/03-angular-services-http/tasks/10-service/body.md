The search term is needed in more than one place: `BooksPage{:ts}` filters with it and every `BookCard{:ts}` highlights it. Instead of passing it down through inputs, we move it into a service that both components can inject.

---

- **Generate the service** Execute the following Angular CLI command: `ng generate service books/book-marker-store{:bash}`.

---

- **Hold the mark term** In _book-marker-store.ts_ add a private `#markTerm{:ts}` signal whose initial value comes from `localStorage.getItem('books.markTerm') ?? ''{:ts}`. Expose it read-only as `markTerm = this.#markTerm.asReadonly(){:ts}` and add a method `setMarkTerm(markTerm: string){:ts}` that sets the private signal.

---

- **Move the persistence** Move the `effect{:ts}` that writes to `localStorage{:ts}` from _BooksPage_ into a `constructor{:ts}` of the service. Persist `markTerm(){:ts}` under the key `books.markTerm`.

---

- **Use the service in `BooksPage{:ts}`** Remove the `searchTerm{:ts}` signal and the `constructor{:ts}` with its `effect{:ts}` from _BooksPage_. Inject `BookMarkerStore{:ts}` using `inject(){:ts}` and read `markTerm(){:ts}` inside `booksComputed{:ts}` instead of `searchTerm(){:ts}`. In _books-page.html_ bind the search field with `[value]{:html}` to `bookMarkerStore.markTerm(){:ts}` and call `bookMarkerStore.setMarkTerm($event.target.value){:ts}` on `(input){:html}`.

---

- **Use the service in `BookCard{:ts}`** Remove the `markTerm{:ts}` input from _BookCard_ and inject `BookMarkerStore{:ts}` instead. In _book-card.html_ pass `bookMarkerStore.markTerm(){:ts}` to the `[markTerm]{:html}` binding of the directive.

---

- **Rename the directive** To match the new service name, rename `Marker{:ts}` to `BookMarker{:ts}`: rename the file _marker.ts_ to _book-marker.ts_, the class to `BookMarker{:ts}` and the selector to `[appBookMarker]{:html}`. Update the usages in _book-card.ts_ and _book-card.html_.

---

- **Check the result** Open the browser at [localhost:4200](http://localhost:4200), type a search term and reload the page. The filter, the highlighting and the stored value should still work.
