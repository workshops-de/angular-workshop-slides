Our book cards show the publishing date via `toLocaleDateString(){:ts}`. The result depends on the browser and can not be controlled by our app.
Let's use a pipe to format the date and make the output independent of the browser settings.

- **Use the `date{:ts}` pipe** Open _src/app/books/book-card/book-card.html_ and replace `currentBook.publishedAt.toLocaleDateString(){:ts}` with the `date{:ts}` pipe. Use the format `'longDate'{:ts}`.
- **Import the pipe** Switch to _src/app/books/book-card/book-card.ts_ and add `DatePipe{:ts}` from `@angular/common` to the `imports{:ts}` of the component.

---

- **Provide the locale** Open _src/app/app.config.ts_ and provide `LOCALE_ID{:ts}` with the value `'de'{:ts}`, so the whole app formats dates the German way.
- **Register the locale data** Angular ships only the `en-US` data by default. Open _src/main.ts_, import the German locale data from `@angular/common/locales/de` and register it with `registerLocaleData(){:ts}` before the app is bootstrapped.

---

- **Check the result** Open the browser at [localhost:4200](http://localhost:4200) and check if the publishing dates are rendered in German, e.g. _5. Mai 2020_.
