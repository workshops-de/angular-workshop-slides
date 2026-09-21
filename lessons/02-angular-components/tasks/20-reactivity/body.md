Let's warm up a bit and get familiar with our project by taking a first look at Angular's reactivity model.

- **Meet the App component** Open your editor and switch to _src/app/app.ts_. You will find a `signal{:ts}` property called `warmWelcome{:ts}`. Switch to _src/app/app.html_ and see how its value is read in the template via `warmWelcome(){:ts}`.

---

- **Add a second signal** In _app.ts_ add another `signal{:ts}` property called `greet{:ts}`, initialized with the value `'Hello'{:ts}`.

---

- **Update a signal from a `constructor{:ts}`** Still in _app.ts_, add a `constructor{:ts}`. Inside, call `setTimeout{:ts}` with a delay of `6000` milliseconds. In its callback, update `warmWelcome{:ts}` using `.update(...){:ts}`, combining the current value with `greet(){:ts}`.

---

- **Adjust the welcome text** Switch to _src/app/workshop-support/shell/welcome/welcome.html_ and remove the hardcoded `Hello,` text, since the greeting will now come from the signal itself.

---

- **Check the result** Open the browser at [localhost:4200](http://localhost:4200). Recognize that the welcome text changes on its own after 6 seconds — without you writing any code to re-render the template. That's Angular's reactivity model at work: the template automatically reacts whenever a signal it reads changes.
