Filtering the list is good - showing _why_ a book matched is better. Wrapping the matching letters in a `<mark>` element is DOM work, so it belongs in an attribute directive that manipulates its host element.

---

- **Generate the directive** Run `ng generate directive books/marker`. It gets the selector `[appMarker]`.

---

- **Add the inputs** Give `Marker` two `input`s: `rawText` (`input.required<string | undefined>()`, the text to render) and `markTerm` (`input('')`, the current search term).

---

- **Render the highlighted text** Inject `Renderer2` and `ElementRef`. In an `effect`, split `rawText()` on `markTerm()`, clear the host element's content and append the segments - plain text nodes for misses, a `<mark class="mark-hit">` wrapper for hits. A prepared helper `classifyMarkSegments(rawText, markTerm)` from `@workshop-support` returns the segments for you.

---

- **Use the directive in `BookCard`** In _book-card.ts_ add a `markTerm = input('')` and register `Marker` in `imports`. In _book-card.html_ replace the interpolated `title` and `author` with `appMarker`, passing `[rawText]` and `[markTerm]`.

---

- **Forward the search term** In _books-page.html_ pass `[markTerm]="searchTerm()"` to `<app-book-card>`.

---

- **Check the result** Search for part of a title - the matching letters should be highlighted in every card.
