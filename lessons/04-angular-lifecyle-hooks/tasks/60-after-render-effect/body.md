The `Marker{:ts}` directive already highlights search matches by writing directly to the DOM — but it does that inside a plain `effect(){:ts}`, which gives no guarantee about *when* during rendering that write happens. Let's fix that with `afterRenderEffect{:ts}`.

---

- **Swap `effect{:ts}` for `afterRenderEffect{:ts}`** In `marker.ts`, replace the `effect(...){:ts}` call in the constructor with `afterRenderEffect(...){:ts}` and update the import from `@angular/core`. The body of `markText{:ts}` stays exactly the same — only the hook around it changes.

---

- **Pick the right phase** A plain callback runs in the `mixedReadWrite{:ts}` phase. `markText{:ts}` only writes to the DOM, so pass an object with a `write{:ts}` callback instead: `afterRenderEffect({ write: () => ... }){:ts}`.

---

- **Check the result** Type into the books search field and confirm matches are still wrapped in `<mark>{:html}` exactly as before.
