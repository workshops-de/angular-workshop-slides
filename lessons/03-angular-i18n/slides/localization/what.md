---
layout: little-what
---

`@angular/localize` offers translations at compile-time, that
are highly performant and backed by `@angular/cli`.

---
layout: default
---

# Compile-time vs runtime translations

| Feature             | XLF               | JSON             |
| ------------------- | ----------------- | ---------------- |
| Standardization     | Industry standard | General-purpose  |
| Metadata support    | Rich              | Limited          |
| ICU expressions     | Native            | Manual           |
| Tool support        | Yes               | Yes              |
| Runtime switching   | Limited           | Yes              |
| Performance         | Optimized         | Runtime overhead |
| Complexity          | Higher            | Lower            |
| Angular integration | Native            | Third-party      |

---
layout: default
---

# What are ICU expression?

- Pluralization: Handle singular/plural forms
  - `{count, plural, =0 {no items} =1 {one item} other {# items}}`
- Gender selection: Choose text based on gender
  - `{gender, select, male {He} female {She} other {They}}`
- Number formatting: Format numbers by locale
  - `{value, number, currency}`
- Date/time formatting: Format dates and times
  - `{date, date, short}`

---
layout: default
---

# Why ICO expressions matter

- Languages handle plurals differently (e.g., some have more than two forms)
- Gender rules vary by language
- Number/date formats differ by locale

---
layout: default
---

# What does XLF stand for?

- XML Localization Interchange File Format

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<xliff version="1.2" xmlns="urn:oasis:names:tc:xliff:document:1.2">
  <file source-language="en-US" datatype="plaintext" original="ng2.template">
    <body>
      <trans-unit id="introductionHeader" datatype="html">
        <source>Hello i18n!</source>
        <target>Bonjour i18n !</target>
        <note priority="1" from="description">An introduction header for this sample</note>
        <note priority="1" from="meaning">User welcome</note>
      </trans-unit>
    </body>
  </file>
</xliff>
```
