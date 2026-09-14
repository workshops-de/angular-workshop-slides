## The functional interceptor

```ts
// error-interceptor.ts
import {
  HttpErrorResponse,
  type HttpHandlerFn,
  type HttpRequest
} from '@angular/common/http';
import { inject } from '@angular/core';
import { catchError, throwError } from 'rxjs';

import { Notifier } from '@workshop-support';

export function errorInterceptor(
  req: HttpRequest<unknown>,
  next: HttpHandlerFn
) {
  const notifier = inject(Notifier);

  return next(req).pipe(
    catchError(error => {
      if (error instanceof HttpErrorResponse) {
        notifier.error(`Request failed: ${error.status} ${error.statusText}`);
      }
      return throwError(() => error);
    })
  );
}
```

Note that `inject()` works here because Angular runs interceptors inside an injection context - no constructor needed.

---

## Registering it

```ts
// app.config.ts
import { provideHttpClient, withInterceptors } from '@angular/common/http';

import { errorInterceptor } from './lib/error-interceptor';

export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(withInterceptors([errorInterceptor]))
    // ...
  ]
};
```

`Notifier` already renders its toasts via CDK Overlay - no template markup needed, just inject and call `.error()` / `.success()` / `.info()`.
