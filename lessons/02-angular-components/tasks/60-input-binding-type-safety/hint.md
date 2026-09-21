## Typing the input signal

`input.required<Book>(){:ts}` removes the `undefined{:ts}` case entirely — the signal always resolves to a `Book{:ts}`.

```ts
// app.ts
book = signal<Book>({ /* ... */ });

// book-card.ts
readonly content = input.required<Book>();
```
