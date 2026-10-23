Users should not lose their input by accident. A `canDeactivate{:ts}`-Guard asks before they leave the create page.

> This is a **simple** guard: it only knows `BookCreatePage{:ts}`, and the page always reports unsaved changes for now. The Submission task in the forms lesson makes it smarter.

---

- **Add the unsaved-changes state** In _book-create-page.ts_ add `readonly hasUnsavedChanges = signal(true);{:ts}`. It is hard-coded for now, so the guard has something to react to — the Submission task sets it to `false{:ts}` once the book is saved.

---

- **Generate the guard** Run `ng generate guard books/confirm-leave --implements CanDeactivate --skip-tests{:bash}`. The CLI creates _books/confirm-leave-guard.ts_ with a function `confirmLeaveGuard{:ts}` of type `CanDeactivateFn<unknown>{:ts}`.

---

- **Implement the guard** The guard receives the component that is about to be left as its first parameter `component{:ts}`. Check with `component instanceof BookCreatePage{:ts}` whether it is the create page and whether `component.hasUnsavedChanges(){:ts}` is `true{:ts}`. In that case ask with `window.confirm(){:ts}` and return the answer. In every other case return `true{:ts}`, so leaving is allowed right away.

---

- **Wire up the guard** Open _book.routes.ts_, import `confirmLeaveGuard{:ts}` and add it with `canDeactivate: [confirmLeaveGuard]{:ts}` to the `create{:ts}`-Route.

---

- **Check the result** Open the create page and navigate to another page. A dialog asks whether you really want to leave. _Cancel_ keeps you on the page, _OK_ lets you go.
