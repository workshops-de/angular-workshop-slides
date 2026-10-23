Our book card gets interactive: let's react to a click on the details link.

---

- **Bind the click event** Open _src/app/books/book-card/book-card.html_, bind to the event `click{:ts}` of the `<a>{:html}`-Tag (aka. Detailslink), and assign the method `handleDetailClick($event){:ts}` to the Event-Binding.

---

- **Implement the handler** Switch to the component class and implement the new method `handleDetailClick(click: MouseEvent){:ts}`. Log the value of the parameter `handleDetailClick{:ts}` to the console and prevent the page from reloading by preventing the default behaviour of the link's click event _(see hint)_.

---

- **Check the result** Open your app at [localhost:4200](http://localhost:4200) and click the details link. The browser's console shows the log messages.
