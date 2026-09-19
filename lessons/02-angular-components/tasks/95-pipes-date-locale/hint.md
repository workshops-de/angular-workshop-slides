## Formatting the date with the `date` pipe

```html
<!-- src/app/books/book-card/book-card.html -->
<p class="book-published">{{ currentBook.publishedAt | date: 'longDate' }}</p>
```

## Importing the pipe

```ts
// src/app/books/book-card/book-card.ts
import { DatePipe } from '@angular/common';

@Component({
  selector: 'app-book-card',
  templateUrl: './book-card.html',
  imports: [DatePipe]
})
export class BookCard {
  // ...
}
```

## Providing the locale

```ts
// src/app/app.config.ts
import { ApplicationConfig, LOCALE_ID } from '@angular/core';

export const appConfig: ApplicationConfig = {
  providers: [{ provide: LOCALE_ID, useValue: 'de' }]
};
```

## Registering the locale data

```ts
// src/main.ts
import { registerLocaleData } from '@angular/common';
import localeDe from '@angular/common/locales/de';
import { bootstrapApplication } from '@angular/platform-browser';
import { App } from './app/app';
import { appConfig } from './app/app.config';

registerLocaleData(localeDe);

bootstrapApplication(App, appConfig).catch(err => console.error(err));
```
