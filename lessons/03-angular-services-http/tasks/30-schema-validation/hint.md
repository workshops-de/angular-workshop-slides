## Install valibot

```bash
npm install valibot
```

---

## The schema

```ts
// book.ts
import * as v from 'valibot';

const BookSchema = v.object({
  id: v.optional(v.pipe(v.string(), v.uuid())),
  isbn: v.string(),
  title: v.string(),
  subtitle: v.optional(v.string()),
  abstract: v.optional(v.string()),
  author: v.optional(v.string()),
  price: v.optional(v.pipe(v.number(), v.minValue(0))),
  numPages: v.optional(v.pipe(v.number(), v.integer(), v.minValue(0))),
  cover: v.optional(v.string()),
  publishedAt: v.optional(
    v.nullable(
      v.pipe(
        v.string(),
        v.transform(isoDate => new Date(isoDate))
      )
    )
  ),
  coAuthors: v.optional(v.array(v.string()))
});

export const BooksCollectionSchema = v.array(BookSchema);

export type Book = v.InferOutput<typeof BookSchema>;
```

---

## Parsing in the client

```ts
// books-client.ts
import * as v from 'valibot';
import { Book, BooksCollectionSchema } from './book';

// httpResource(...) second argument:
{
  defaultValue: [],
  parse: value => v.parse(BooksCollectionSchema, value)
}
```
