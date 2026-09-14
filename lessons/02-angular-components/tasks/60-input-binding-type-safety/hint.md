## Typing the input signal

`input.required<Book>()` removes the `undefined` case entirely — the signal always resolves to a `Book`.

```ts
// app.ts
book = signal<Book>({ /* ... */ });

// book-card.ts
readonly content = input.required<Book>();
```
