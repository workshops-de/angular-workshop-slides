The `Marker` directive already highlights search matches by writing directly to the DOM — but it does that inside a plain `effect()`, which gives no guarantee about *when* during rendering that write happens. Let's fix that with `afterRenderEffect`.

---

- **Swap `effect` for `afterRenderEffect`** In `marker.ts`, replace the `effect(...)` call in the constructor with `afterRenderEffect(...)` and update the import from `@angular/core`. The body of `markText` stays exactly the same — only the hook around it changes.

---

- **Check the result** Type into the books search field and confirm matches are still wrapped in `<mark>` exactly as before.
