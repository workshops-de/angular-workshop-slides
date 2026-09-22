<details>
<summary>Annotate `App{:ts}`</summary>

```ts
// app.ts
book = signal<Book>({ /* ... */ });
```

</details>

<details>
<summary>Annotate `BookCard{:ts}`</summary>

`input.required<Book>(){:ts}` removes the `undefined{:ts}` case entirely — the signal always resolves to a `Book{:ts}`.

```ts
// book-card.ts
readonly content = input.required<Book>();
```

</details>
