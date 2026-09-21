Filtering the list is good - showing _why_ a book matched is better. Wrapping the matching letters in a `<mark>{:html}` element is DOM work, so it belongs in an attribute directive that manipulates its host element.

---

- **Generate the directive** Run `ng generate directive books/marker{:bash}`. It gets the selector `[appMarker]{:html}`.

---

- **Add the inputs** Give `Marker{:ts}` two `input{:ts}`s: `rawText{:ts}` (`input.required<string | undefined>(){:ts}`, the text to render) and `markTerm{:ts}` (`input(''){:ts}`, the current search term).

---

- **Render the highlighted text** Inject `Renderer2{:ts}` and `ElementRef{:ts}`. In an `effect{:ts}`, split `rawText(){:ts}` on `markTerm(){:ts}`, clear the host element's content and append the segments - plain text nodes for misses, a `<mark class="mark-hit">{:html}` wrapper for hits. A prepared helper `classifyMarkSegments(rawText, markTerm){:ts}` from `@workshop-support` returns the segments for you.

---

- **Use the directive in `BookCard{:ts}`** In _book-card.ts_ add a `markTerm = input(''){:ts}` and register `Marker{:ts}` in `imports{:ts}`. In _book-card.html_ replace the interpolated `title{:ts}` and `author{:ts}` with `appMarker{:ts}`, passing `[rawText]{:html}` and `[markTerm]{:html}`.

---

- **Forward the search term** In _books-page.html_ pass `[markTerm]="searchTerm()"{:html}` to `<app-book-card>{:html}`.

---

- **Check the result** Search for part of a title - the matching letters should be highlighted in every card.
