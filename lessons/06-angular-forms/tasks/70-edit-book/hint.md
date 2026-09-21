```typescript
// book.routes.ts
{
  path: 'edit/:isbn',
  loadComponent: () => import('./book-edit-page/book-edit-page').then(c => c.BookEditPage)
}
```

```typescript
// books-client.ts
import { httpResource } from '@angular/common/http';
import { Signal } from '@angular/core';

getByIsbnResource(isbn: Signal<string>) {
  return httpResource<Book>(() => ({ url: `${this.#baseUrl}/books/${isbn()}` }));
}
```

```typescript
// book-edit-page.ts
import { Component, inject, input } from '@angular/core';
import { Book } from '../book';
import { BookEditForm } from '../book-edit-form/book-edit-form';
import { BooksClient } from '../books-client';

@Component({
  selector: 'app-book-edit-page',
  imports: [BookEditForm],
  templateUrl: './book-edit-page.html'
})
export class BookEditPage {
  private readonly booksClient = inject(BooksClient);

  readonly isbn = input.required<string>();

  protected readonly bookResource = this.booksClient.getByIsbnResource(this.isbn);

  protected saveBook(book: Book) {
    this.booksClient.update(book.isbn, book).subscribe();
  }
}
```

```html
<!-- book-edit-page.html -->
@if (bookResource.isLoading()) {
  <p>Loading book...</p>
} @else if (bookResource.error(); as error) {
  <p>Error: {{ error.message }}</p>
} @else if (bookResource.value(); as book) {
  <app-book-edit-form [book]="book" (save)="saveBook($event)" />
}
```

```typescript
// book-edit-form.ts
import { Component, input, linkedSignal, output } from '@angular/core';
import { form, FormField, FormRoot, readonly, required } from '@angular/forms/signals';
import { Book } from '../book';
import { validAuthorName } from '../validators/author';

const PLACEHOLDER_COVER = 'book-cover-placeholder.svg';

// Optional Book fields need a value so every field in the form has something to bind to.
const emptyBookForm = { isbn: '', title: '', subtitle: '', author: '', abstract: '', cover: '' };

@Component({
  selector: 'app-book-edit-form',
  imports: [FormField, FormRoot],
  templateUrl: './book-edit-form.html'
})
export class BookEditForm {
  readonly book = input.required<Book>();
  readonly save = output<Book>();

  protected readonly placeholderCover = PLACEHOLDER_COVER;

  // Inputs are read-only, so the form edits a writable copy.
  protected readonly model = linkedSignal(() => ({ ...emptyBookForm, ...this.book() }));

  protected readonly form = form(
    this.model,
    schemaPath => {
      readonly(schemaPath.isbn);
      required(schemaPath.title, { message: 'Please insert a title.' });
      required(schemaPath.author, { message: 'Please insert an Author.' });
      validAuthorName(schemaPath.author);
    },
    {
      submission: {
        // Only announce the edited book - sending it is up to the parent.
        action: async () => {
          this.save.emit(this.model());
          return null;
        }
      }
    }
  );
}
```

```html
<!-- book-edit-form.html -->
<div class="app-content">
  <h1 class="page-title">Edit Book</h1>

  <form class="form-fields" [formRoot]="form">
    <label class="field-label">
      <span class="field-label-text">ISBN</span>
      <input class="field-input w-full bg-gray-100 text-gray-500" [formField]="form.isbn" />
      <small class="field-hint">The ISBN cannot be changed after a book has been created.</small>
    </label>

    <label class="field-label">
      <span class="field-label-text">Title</span>
      <input class="field-input w-full" [formField]="form.title" />
      @if (form.title().touched()) {
        @for (error of form.title().errors(); track error.kind) {
          <small class="field-error">{{ error.message }}</small>
        }
      }
    </label>

    <label class="field-label">
      <span class="field-label-text">Subtitle</span>
      <input class="field-input w-full" [formField]="form.subtitle" />
    </label>

    <label class="field-label">
      <span class="field-label-text">Author</span>
      <input class="field-input w-full" [formField]="form.author" />
      @if (form.author().touched()) {
        @for (error of form.author().errors(); track error.kind) {
          <small class="field-error">{{ error.message }}</small>
        }
      }
    </label>

    <label class="field-label">
      <span class="field-label-text">Cover URL</span>
      <input
        class="field-input w-full"
        [formField]="form.cover"
        placeholder="https://example.com/cover.jpg"
      />
    </label>

    <div class="cover-preview">
      <img
        class="cover-preview-image"
        [src]="model().cover || placeholderCover"
        alt="Cover preview"
      />
      <div>
        <span class="cover-preview-label">Cover preview</span>
        <p class="field-hint">
          Updates as you type the URL. Falls back to the placeholder when the URL is empty.
        </p>
      </div>
    </div>

    <label class="field-label">
      <span class="field-label-text">Abstract</span>
      <textarea class="field-input w-full" [formField]="form.abstract" rows="4"></textarea>
    </label>

    <div class="form-actions">
      <button type="submit" class="btn-primary" [disabled]="form().invalid()">Save</button>
    </div>
  </form>
</div>
```
