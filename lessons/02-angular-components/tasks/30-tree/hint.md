## Importing BookCard into App

Add `BookCard` to the `imports` array of the `@Component` decorator so its selector `app-book-card` becomes available in the template.

```ts
@Component({
  selector: 'app-root',
  imports: [BookCard],
  templateUrl: './app.html'
})
```
