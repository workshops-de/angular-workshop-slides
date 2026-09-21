Network hiccups shouldn't immediately show an error toast. Let's retry failed requests a couple of times first.

---

- **Add a retry** In `errorInterceptor{:ts}`, pipe `next(req){:ts}` through the `retry{:ts}` operator from `rxjs` before `catchError{:ts}` - configure it with `{ count: 2, delay: 500 }{:ts}` so a failed request is tried up to two more times, 500ms apart.

---

- **Only retry network errors** Pass a `delay{:ts}` function to `retry{:ts}` instead of a plain number: check `error.status === 0{:ts}` (no connection) and return `timer(500){:ts}` to retry, otherwise `throw error{:ts}` to skip straight to `catchError{:ts}`. That way a `404` shows the toast immediately, while a dropped connection gets a second chance.

---

- **Check the result** Stop the API server, trigger a request, and watch the network tab - you should see up to three attempts before the error toast appears.
