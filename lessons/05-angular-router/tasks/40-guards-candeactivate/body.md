- **Add unsaved-changes state** In `BookCreatePage{:ts}`, add a `readonly hasUnsafeChanges = signal(true);{:ts}` (hard-coded for this exercise so the guard has something to react to — a later exercise derives it from the form's own dirty state).

---

- **Create a guard function** `ng generate guard books/confirm-leave{:bash}`.
- Use `window.confirm{:ts}` to ask the user if he really wants to leave the page — but only if `hasUnsafeChanges(){:ts}` is `true{:ts}`, otherwise allow leaving right away.

---

- **Wire up the guard** Open `book.routes.ts`.
- Add the guard to the `create{:ts}`-Route (component: `BookCreatePage{:ts}`).
