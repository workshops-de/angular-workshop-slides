- **Create the user state** Create a service `UserState{:ts}` in _src/app/user-state.ts_ with `@Service(){:ts}`. It holds the login state as a signal: `readonly isLoggedIn = signal(true){:ts}`.

---

- **Create a `canMatch{:ts}`-Guard** Create a guard function `isUserAuthenticatedGuardFn{:ts}` of type `CanMatchFn{:ts}` in _src/app/is-user-authenticated.ts_. Inject `UserState{:ts}` and return the value of `isLoggedIn(){:ts}`. Register the guard with `canMatch{:ts}` on the **books** route in _app.routes.ts_.

---

- **Check the result** Open [localhost:4200/books](http://localhost:4200/books): you should see the book page. Now set `isLoggedIn{:ts}` to `signal(false){:ts}` and reload.

> If you are not logged in, it should show the error `NG04002: Cannot match any routes.` in the browser console. If you are logged in, it should show the book page.
