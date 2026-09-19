## Swap `effect` for `afterRenderEffect`

```ts
// marker.ts
import { Directive, ElementRef, Renderer2, afterRenderEffect, inject, input } from '@angular/core';

import { classifyMarkSegments } from '@workshop-support';

@Directive({ selector: '[appMarker]' })
export class Marker {
  private renderer = inject(Renderer2);
  private host = inject<ElementRef<HTMLElement>>(ElementRef);

  rawText = input.required<string | undefined>();
  markTerm = input('');

  constructor() {
    afterRenderEffect({
      write: () => this.markText(this.rawText(), this.markTerm())
    });
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

Only the constructor changed. `markText` still reads `rawText()`/`markTerm()` and writes to the DOM via `Renderer2` — but now that write runs in the `write` phase after rendering instead of in an unordered `effect()`.

## Why `write`?

`afterRenderEffect(() => ...)` without phases runs in `mixedReadWrite`, which Angular recommends avoiding when the work can be split. `markText` never reads layout from the DOM, so `write` is the fitting phase.

---

## Check the result

Type a few letters into the books search field. The matching parts of each title should still be wrapped in `<mark class="mark-hit">`, same as before the refactor.
