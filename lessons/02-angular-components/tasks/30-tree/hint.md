## Importing BookCard into App

Add `BookCard{:ts}` to the `imports{:ts}` array of the `@Component{:ts}` decorator so its selector `app-book-card` becomes available in the template.

```ts
@Component({
  selector: 'app-root',
  imports: [BookCard],
  templateUrl: './app.html'
})
```
