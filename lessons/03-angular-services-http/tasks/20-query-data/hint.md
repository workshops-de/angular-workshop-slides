## API starten
If not already installed
```bash
# run bookmonkey-api directly
npx bookmonkey-api
```

## Providing HttpClient

```typescript
import { provideHttpClient } from '@angular/common/http';

providers: [provideHttpClient()]
```

## Loading books in BooksClient

```typescript
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
```

```typescript
return this.http.get<Book[]>('http://localhost:4730/books')
```

## Consuming the Observable in App

Bridge the Observable to a signal with `toSignal` so the template keeps working:

```typescript
// app.ts
import { toSignal } from '@angular/core/rxjs-interop';

books = toSignal(this.booksClient.getAll(), { initialValue: [] });
```
