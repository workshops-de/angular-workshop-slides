Network hiccups shouldn't immediately show an error toast. Let's retry failed requests a couple of times first.

---

- **Add a retry** In `errorInterceptor`, pipe `next(req)` through the `retry` operator from `rxjs` before `catchError` - configure it with `{ count: 2, delay: 500 }` so a failed request is tried up to two more times, 500ms apart.

---

- **Only retry network errors** Pass a `delay` function to `retry` instead of a plain number: check `error.status === 0` (no connection) and return `timer(500)` to retry, otherwise `throw error` to skip straight to `catchError`. That way a `404` shows the toast immediately, while a dropped connection gets a second chance.

---

- **Check the result** Stop the API server, trigger a request, and watch the network tab - you should see up to three attempts before the error toast appears.
