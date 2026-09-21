Right now a failed request just disappears silently in the console. Let's catch every failed HTTP call in one central place and show the user a toast instead.

---

- **Create a functional interceptor** Add `error-interceptor.ts` in `src/app/lib` and export a function `errorInterceptor(req: HttpRequest<unknown>, next: HttpHandlerFn){:ts}`. Call `next(req){:ts}` and use the `catchError{:ts}` operator from `rxjs` to react to failures.

---

- **Show a toast on failure** Inject the `Notifier{:ts}` from `@workshop-support`. Inside `catchError{:ts}`, check with `error instanceof HttpErrorResponse{:ts}` and call `notifier.error(...){:ts}` with a message that includes `error.status{:ts}` and `error.statusText{:ts}`. Re-throw the error afterwards with `throwError(() => error){:ts}` so callers still see it.

---

- **Register the interceptor** In `app.config.ts` pass `withInterceptors([errorInterceptor]){:ts}` to `provideHttpClient(...){:ts}`.

---

- **Provoke an HTTP error** Add the query parameter `_devError{:ts}` to the request that loads the books in `book-client.ts`. `_devError: true{:ts}` causes a 400 error which makes your `errorInterceptor{:ts}` to show an error notification

---

- **Check the result** Confirm a toast with the error status pops up.
