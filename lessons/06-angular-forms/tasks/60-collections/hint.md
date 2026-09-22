```typescript
// book-create-form.ts
import { applyEach, form, FormField, FormRoot, required } from '@angular/forms/signals';

export class BookCreateForm {
  // The form model mirrors the Book payload, so submission can hand it straight
  // to the API. `author` stays a single value, `coAuthors` is the collection.
  protected readonly model = signal({
    isbn: '',
    title: '',
    subtitle: '',
    author: '',
    coAuthors: [] as string[],
    abstract: '',
    cover: ''
  });

  protected readonly form = form(
    this.model,
    schemaPath => {
      required(schemaPath.isbn, { message: 'Please insert an ISBN.' });
      required(schemaPath.title, { message: 'Please insert a title.' });
      required(schemaPath.author, { message: 'Please insert an Author.' });
      validAuthorName(schemaPath.author);
      applyEach(schemaPath.coAuthors, coAuthor => {
        required(coAuthor, { message: 'Please insert a co-author name.' });
        validAuthorName(coAuthor);
      });
    },
    { submission: { ... } }
  );

  addCoAuthor() {
    this.model.update(m => ({ ...m, coAuthors: [...m.coAuthors, ''] }));
  }

  removeCoAuthor(coAuthorIndex: number) {
    this.model.update(m => ({
      ...m,
      coAuthors: m.coAuthors.filter((_, i) => i !== coAuthorIndex)
    }));
  }
}
```

```html
<fieldset class="field-collection">
  <legend class="field-label-text">Co-authors</legend>

  @for (coAuthor of form.coAuthors; track $index; let coAuthorIndex = $index) {
    <div class="field-collection-row">
      <input class="field-input min-w-0 flex-1" [formField]="coAuthor" placeholder="Co-author name" />
      <button type="button" class="btn-icon-danger" (click)="removeCoAuthor(coAuthorIndex)" aria-label="Remove co-author">
        ✕
      </button>
    </div>
    @if (coAuthor().touched()) {
      @for (error of coAuthor().errors(); track error.kind) {
        <small class="field-error">{{ error.message }}</small>
      }
    }
  } @empty {
    <p class="field-hint">No co-authors yet.</p>
  }

  <button type="button" class="btn-secondary btn-add" (click)="addCoAuthor()">+ Add co-author</button>
</fieldset>
```
