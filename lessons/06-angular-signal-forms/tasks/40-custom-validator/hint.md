```typescript
// validators/author.ts
import { SchemaPath, validate } from '@angular/forms/signals';

export function validAuthorName(schemaPath: SchemaPath<string>): void {
  validate(schemaPath, field => {
    const authorName = field.value();

    if (!authorName) return null;

    const hasNumeric = /[0-9]+/.test(authorName);
    return hasNumeric ? { kind: 'invalidAuthor', message: 'Name must not contain digits' } : null;
  });
}
```

```typescript
// book-new-page.ts
import { validAuthorName } from '../validators/author';

protected readonly form = form(this.model, schemaPath => {
  required(schemaPath.author, { message: 'Please insert an Author.' });
  validAuthorName(schemaPath.author);
  ....
});
```
