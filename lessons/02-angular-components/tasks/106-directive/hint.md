<details>
<summary>Generate the directive</summary>

```bash
ng generate directive books/marker
```

</details>

<details>
<summary>Render the highlighted text</summary>

```ts
// marker.ts
import { Directive, ElementRef, Renderer2, effect, inject, input } from '@angular/core';
import { classifyMarkSegments } from '@workshop-support';

@Directive({ selector: '[appMarker]' })
export class Marker {
  private renderer = inject(Renderer2);
  private host = inject<ElementRef<HTMLElement>>(ElementRef);

  rawText = input.required<string | undefined>();
  markTerm = input('');

  constructor() {
    effect(() => this.markText(this.rawText(), this.markTerm()));
  }

  private markText(rawText: string | undefined, markTerm: string) {
    const segments = classifyMarkSegments(rawText, markTerm);

    this.renderer.setProperty(this.host.nativeElement, 'textContent', '');

    for (const segment of segments) {
      const text = this.renderer.createText(segment.text);
      const child = segment.shouldBeMarked ? this.wrapInMark(text) : text;
      this.renderer.appendChild(this.host.nativeElement, child);
    }
  }

  private wrapInMark(node: HTMLElement) {
    const mark = this.renderer.createElement('mark');
    this.renderer.addClass(mark, 'mark-hit');
    this.renderer.appendChild(mark, node);
    return mark;
  }
}
```

</details>

<details>
<summary>Use the directive in `BookCard{:ts}`</summary>

```html
<!-- book-card.html -->
<h3 appMarker [rawText]="book().title" [markTerm]="markTerm()"></h3>
<h4 [style]="customStyle()" appMarker [rawText]="book().author" [markTerm]="markTerm()"></h4>
```

```ts
// book-card.ts
import { Marker } from '../marker';

@Component({
  selector: 'app-book-card',
  imports: [Marker],
  templateUrl: './book-card.html'
})
export class BookCard {
  readonly markTerm = input('');
}
```

</details>

<details>
<summary>Forward the search term</summary>

```html
<!-- books-page.html -->
<app-book-card
  [book]="book"
  [markTerm]="searchTerm()"
  (detailClick)="goToBookDetails($event)"
  (deleteClick)="deleteBook($event)"
/>
```

</details>
