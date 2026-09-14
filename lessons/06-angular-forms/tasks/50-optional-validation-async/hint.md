```typescript
// validators/isbn.ts
import { HttpErrorResponse } from '@angular/common/http';
import { SchemaPath, validateHttp } from '@angular/forms/signals';

export function uniqueIsbn(path: SchemaPath<string>): void {
  validateHttp(path, {
    request: ({ value }) => `http://localhost:4730/books/${value()}`,
    onSuccess: () => ({ kind: 'duplicateIsbn', message: 'This ISBN already exists' }),
    onError: error =>
      error instanceof HttpErrorResponse && error.status === 404
        ? null
        : { kind: 'checkFailed', message: 'Could not verify ISBN uniqueness' }
  });
}
```

```typescript
// book-new-page.ts
import { uniqueIsbn } from '../validators/isbn';

protected readonly form = form(this.model, schemaPath => {
  required(schemaPath.isbn, { message: 'Please insert an ISBN.' });
  uniqueIsbn(schemaPath.isbn);
  ....
});
```

```html
@if (form.isbn().pending()) {
  <small>Checking ISBN…</small>
} @else if (form.isbn().touched()) {
  @for (error of form.isbn().errors(); track error.kind) {
    <small>{{ error.message }}</small>
  }
}
```
