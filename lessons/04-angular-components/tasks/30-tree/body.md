3, 2, 1 Go! Now you will create your first component.

- **Generate the component** Open a second terminal, switch to the directory where your Angular project is located, and execute `ng generate component books/book-card`. Recognize that two files are generated and that your component (_book-card.ts_) has the selector `app-book-card`.

- **Build a static template** Open _src/app/books/book-card/book-card.html_ and set up a simple HTML template visualizing book-information by using **static data**.
  - title
  - author
  - details-link
  - abstract

  ```html
  <!-- book-card.html -->

  <h3>Moby Dick</h3>
  <h4>Herman Melville</h4>

  <!--
  ... link, abstract ...
  -->
  ```

---

- **Use the component in _App_** Use your component in _app.html_. Replace the existing content of _app.html_ with `<app-book-card />`. Add the missing import for `BookCard` to imports in _app.ts_.
- **Verify** Ensure that your component is displayed in the browser. Check [localhost:4200](http://localhost:4200).

## How the component could look like

<iframe src="https://docs.google.com/presentation/d/1QyM9Nwm6CRvQkDvp3q9I-UN32CQmZ-eXs9tdBJXeFYk/embed#slide=id.ga8afa0fa9e_0_24" width="100%" height="720px"></iframe>
