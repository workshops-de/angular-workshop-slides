Right now a failed request just disappears silently in the console. Let's catch every failed HTTP call in one central place and show the user a toast instead.

---

- **Create a functional interceptor** Add `error-interceptor.ts` in `src/app/lib` and export a function `errorInterceptor(req: HttpRequest<unknown>, next: HttpHandlerFn)`. Call `next(req)` and use the `catchError` operator from `rxjs` to react to failures.

---

- **Show a toast on failure** Inject the `Notifier` from `@workshop-support`. Inside `catchError`, check with `error instanceof HttpErrorResponse` and call `notifier.error(...)` with a message that includes `error.status` and `error.statusText`. Re-throw the error afterwards with `throwError(() => error)` so callers still see it.

---

- **Register the interceptor** In `app.config.ts` pass `withInterceptors([errorInterceptor])` to `provideHttpClient(...)`.

---

- **Check the result** Trigger a failing request (e.g. delete a book twice, or stop the API server) and confirm a toast with the error status pops up in the bottom right corner.
