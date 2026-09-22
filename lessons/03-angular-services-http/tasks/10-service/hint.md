<details>
<summary>Generate the service</summary>

```bash
ng generate service books/books-client
```

</details>

<details>
<summary>Use the service in `App{:ts}`</summary>

```typescript
// app.ts
private readonly booksClient = inject(BooksClient);
```

</details>
