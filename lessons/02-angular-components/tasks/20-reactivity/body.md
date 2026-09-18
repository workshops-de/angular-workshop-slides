Let's warm up a bit and get familiar with our project by taking a first look at Angular's reactivity model.

- **Meet the App component** Open your editor and switch to _src/app/app.ts_. You will find a `signal` property called `warmWelcome`. Switch to _src/app/app.html_ and see how its value is read in the template via `warmWelcome()`.

---

- **Add a second signal** In _app.ts_ add another `signal` property called `greet`, initialized with the value `'Hello'`.

---

- **Update a signal from a `constructor`** Still in _app.ts_, add a `constructor`. Inside, call `setTimeout` with a delay of `6000` milliseconds. In its callback, update `warmWelcome` using `.update(...)`, combining the current value with `greet()`.

---

- **Adjust the welcome text** Switch to _src/app/workshop-support/shell/welcome/welcome.html_ and remove the hardcoded `Hello,` text, since the greeting will now come from the signal itself.

---

- **Check the result** Open the browser at [localhost:4200](http://localhost:4200). Recognize that the welcome text changes on its own after 6 seconds — without you writing any code to re-render the template. That's Angular's reactivity model at work: the template automatically reacts whenever a signal it reads changes.
