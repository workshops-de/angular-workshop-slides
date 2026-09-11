```html
<!-- book-card.html -->
<div class="...">
  <ng-content />
  <p>{{ content().abstract }}</p>
</div>
```

```html
<!-- books-page.html -->
<app-book-card [content]="book">
  <a
    [routerLink]="['detail', book.isbn]"
    class="inline-block cursor-pointer rounded border border-gray-300 px-4 py-2 text-gray-700 transition-colors hover:bg-gray-50"
  >
    Details
  </a>
</app-book-card>
```

```typescript
// books-page.ts
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-book',
  imports: [BookCard, RouterLink],
  templateUrl: './books-page.html'
})
export class BooksPage {
  ...
}
```
