---

# Setup

```bash
# maybe needed: npm install @angular/localize --force
npx @angular/cli add @angular/localize
```

<!--
Due to package conflicts sometimes we need to enforce installing a npm package. That's why the npm install --force command is mentioned, here.
-->

---

# Mark translations with `i18n`

````md magic-move
```html
<h1 i18n="@@heading">Hello @angular/localize</h1>
```

```angular-ts
@Component({
  selector: 'my-component',
  template: `
    <h1 i18n="@@heading">Hello @angular/localize</h1>
  `
})
export class MyComponent {}
```
````

---
layout: two-cols-header
layoutClass: gap-8
---

# Extract translations

::left::

```bash
npx @angular/cli extract-i18n --output-path src/locale
```

::right::

```text
src/
└── local/
    ├── messages.xlf
    └── messages.{lang-code}.xlf
```

::bottom::

The CLI command will generate the file structure containing your translations.

---
layout: default
---

# Translate

```xml{*|6|6-7|8-11}
<?xml version="1.0" encoding="UTF-8" ?>
<xliff version="1.2" xmlns="urn:oasis:names:tc:xliff:document:1.2">
  <file source-language="de-de" datatype="plaintext" original="ng2.template">
    <body>
      <trans-unit id="action.book.add" datatype="html">
        <source>Add Book</source>
        <target>Buch hinzufügen</target>
        <context-group purpose="location">
          <context context-type="sourcefile">src/app/app.ts</context>
          <context context-type="linenumber">14,17</context>
        </context-group>
      </trans-unit>
    </body>
  </file>
</xliff>
```

---

# Common Patterns

<div class="grid grid-cols-2 gap-6">

<div>

## Pattern A: Simple

```typescript
// For simple use cases
const result = simple(input);
```

Best for: Quick prototypes

</div>

<div>

## Pattern B: Advanced

```typescript
// For complex scenarios
const result = await advanced({
  input,
  options: { deep: true },
});
```

Best for: Production apps

</div>

</div>
