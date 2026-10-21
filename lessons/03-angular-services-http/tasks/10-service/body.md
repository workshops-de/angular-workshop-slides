The search term is needed in more than one place: `BooksPage{:ts}` filters with it and the marker directive in every `BookCard{:ts}` highlights it. Instead of passing it down through inputs, we move it into a service that both can inject. The service is provided locally by _BooksPage_, so every directive below it shares the same instance.

---

- **Generate the service** Execute the following Angular CLI command: `ng generate service books/book-marker-store{:bash}`.

---

- **Hold the mark term** In _book-marker-store.ts_ change the decorator to `@Service({ autoProvided: false }){:ts}`, because the service will only be provided by _BooksPage_. Add a private `#markTerm{:ts}` signal whose initial value comes from `localStorage.getItem('books.markTerm') ?? ''{:ts}`. Expose it read-only as `markTerm = this.#markTerm.asReadonly(){:ts}` and add a method `setMarkTerm(markTerm: string){:ts}` that sets the private signal.

---

- **Move the persistence** Move the `effect{:ts}` that writes to `localStorage{:ts}` from _BooksPage_ into a `constructor{:ts}` of the service. Persist `markTerm(){:ts}` under the key `books.markTerm`.

---

- **Use the service in `BooksPage{:ts}`** Remove the `searchTerm{:ts}` signal and the `constructor{:ts}` with its `effect{:ts}` from _BooksPage_. Provide `BookMarkerStore{:ts}` locally with `providers: [BookMarkerStore]{:ts}` in the `@Component{:ts}` decorator, inject it using `inject(){:ts}` and read `markTerm(){:ts}` inside `booksComputed{:ts}` instead of `searchTerm(){:ts}`. In _books-page.html_ bind the search field with `[value]{:html}` to `bookMarkerStore.markTerm(){:ts}` and call `bookMarkerStore.setMarkTerm($event.target.value){:ts}` on `(input){:html}`.

---

- **Rename the directive** To match the new service name, rename `Marker{:ts}` to `BookMarker{:ts}`: rename the file _marker.ts_ to _book-marker.ts_, the class to `BookMarker{:ts}` and the selector to `[appBookMarker]{:html}`. Update the usages in _book-card.ts_ and _book-card.html_.

---

- **Use the service in `BookMarker{:ts}`** In _book-marker.ts_ remove the `markTerm{:ts}` input and inject `BookMarkerStore{:ts}` instead. Inside the `effect{:ts}` read `bookMarkerStore.markTerm(){:ts}` instead of the input. Do not provide the service again: the directive receives the instance of _BooksPage_.

---

- **Clean up `BookCard{:ts}`** _BookCard_ no longer needs the mark term. Remove its `markTerm{:ts}` input and remove the `[markTerm]{:html}` bindings from the `appBookMarker{:html}` elements in _book-card.html_.

---

- **Check the result** Open the browser at [localhost:4200](http://localhost:4200), type a search term and reload the page. The filter, the highlighting and the stored value should still work.
