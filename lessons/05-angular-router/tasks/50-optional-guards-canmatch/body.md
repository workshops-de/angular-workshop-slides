- Create a service `UserState` holding the login state if the user is logged in
- Create a guard function (`is-user-authenticated.ts`) as *CanMatchFn* to read that state by injecting that service and allow access on the **books** routes

Result:
- If you are not logged in, it should show the error `NG04002: Cannot match any routes.` in the browser console.
- If you are logged in, it should show the book page.
