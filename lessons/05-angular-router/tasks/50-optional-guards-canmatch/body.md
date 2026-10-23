- **Create the user state** Create a service `UserState{:ts}` in _src/app/user-state.ts_ with `@Service(){:ts}`. It holds the login state as a signal: `readonly isLoggedIn = signal(true){:ts}`.

---

- **Create a `canMatch{:ts}`-Guard** Create a guard function `isUserAuthenticatedGuardFn{:ts}` of type `CanMatchFn{:ts}` in _src/app/is-user-authenticated.ts_. Inject `UserState{:ts}` and return the value of `isLoggedIn(){:ts}`. Register the guard with `canMatch{:ts}` on the **books** route in _app.routes.ts_.

---

- **Check the result** Open [localhost:4200/books](http://localhost:4200/books): you should see the book page. Now set `isLoggedIn{:ts}` to `signal(false){:ts}` and reload. The page stays empty and the browser console shows _NG04002: Cannot match any routes._: the guard rejected the **books** route and no other route matches. (If you added the wildcard route from the bonus of the router setup, you are redirected to the start page instead – the wildcard is the next matching route.)

---

- **Add a fallback route** A rejected `canMatch{:ts}` route does not end the navigation: the router keeps looking for the next matching route. Add a second route with the same path **below** the protected one, displaying `LoginHint{:ts}` (imported from `@workshop-support`).

> The order matters: the router takes the first route that matches. Place the fallback route above the protected one and it would always win.

---

- **Check the result again** Reload [localhost:4200/books](http://localhost:4200/books) with `signal(false){:ts}`: now you see the "Please log in" page instead of the error. Switch back to `signal(true){:ts}` and you see the book page again.
