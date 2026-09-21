Blau-lastige Basispalette, passend zum Akzent des Layouts:

| Token Type                                                                  | RGB (0–1)           | Hex      | Bold |
| :-------------------------------------------------------------------------- | :------------------ | :------- | :--- |
| Keywords (`export`, `class`, `private`, `return`, `this`, `import`, `from`) | 0, 0.0627, 0.502    | \#001080 | Yes  |
| Decorators (`@Injectable`, `@Component`, `@Input`)                          | 0, 0.502, 0.627     | \#0080A0 | No   |
| Types / Method Names / Function Calls (`Book`, `getAll`, `get`, `inject`)   | 0.176, 0.376, 0.792 | \#2D60CA | No   |
| String Literals                                                             | 0, 0.467, 0.667     | \#0077AA | No   |
| Standard Text (Punctuation, operators, remaining code)                      | 0.2, 0.2, 0.2       | \#333333 | No   |

Regeln fürs Highlighting:

- Jedes Schlüsselwort der Sprache (auch `this`, `import`, `from`, `async`,
  `await` etc.) bekommt die Keyword-Farbe **und bold**.
- Jeder Dekorator (alles, was mit `@` beginnt, z. B. `@Injectable`,
  `@Component`, `@Input`) bekommt die Decorator-Farbe, nicht bold.
- Klassennamen, Interfaces, generische Typparameter UND aufgerufene
  Methoden-/Funktionsnamen (auch technische wie `inject(...)`) bekommen
  einheitlich die Typen/Methoden-Farbe — das schafft die visuelle Verbindung
  zwischen Deklaration und Aufruf.
- Nur echte String-Literale bekommen die String-Farbe.
- Alles andere (Klammern, Operatoren, Property-Zugriffe wie `.http.`) bleibt
  im Standardtext-Grau.

## HTML (Angular Templates)

Es gilt dieselbe Palette — HTML bekommt keine eigenen Farben, nur eine Zuordnung
der Token:

| HTML Token                                                                    | Farbe                | Bold |
| :---------------------------------------------------------------------------- | :------------------- | :--- |
| Tag-Namen (`div`, `app-book`, `ng-container`), auch in schließenden Tags      | Types (\#2D60CA)     | No   |
| Attributnamen (`class`, `[value]`, `(click)`, `*ngFor`, `#ref`, `disabled`)   | Decorators (\#0080A0) | No   |
| Control-Flow-Namen (`@if`, `@else if`, `@for`, `@switch`, `@let`, `@defer`)   | Decorators (\#0080A0) | No   |
| Statische Attributwerte (`class="title"`, `type='button'`)                    | Strings (\#0077AA)   | No   |
| Keywords in Ausdrücken (`of`, `as`, `async`, `let`, `track`)                  | Keywords (\#001080)  | Yes  |
| Funktionsaufrufe in Ausdrücken (`select(book)`, `format(price)`)              | Types (\#2D60CA)     | No   |
| Kommentare `<!-- ... -->`                                                     | Grau (\#999999)      | No   |
| Spitze Klammern, `=`, `/`, Anführungszeichen um Binding-Werte, Fließtext      | Standard (\#333333)  | No   |

Regeln fürs HTML-Highlighting:

- **Ausdrücke vs. Fließtext:** Keywords, Funktionsaufrufe, Typen und Strings
  werden nur in _Ausdrücken_ ausgezeichnet: `{{ ... }}`, Werte von Bindings
  (`[x]="…"`, `(x)="…"`, `*x="…"`), Control-Flow-Header (`@if (…)`,
  `@for (…)`) und `@let …;`. Fließtext zwischen den Tags bleibt Standard-Grau —
  ein „in" oder „get" im Text darf nie fett werden.
- **`class` ist in HTML kein Keyword**, sondern ein Attributname
  (Decorator-Farbe, nicht bold).
- **Binding-Werte sind keine Strings:** `[title]="book.title"` und
  `(click)="save()"` werden wie TypeScript-Ausdrücke gefärbt (Klammern und
  Anführungszeichen Standard-Grau). Nur echte String-Literale darin
  (`[title]="'Hello'"`) bekommen die String-Farbe.
- Der `@` bei Control-Flow bleibt wie bei TypeScript-Dekoratoren ungefärbt,
  nur der Name (`if`, `for`, …) bekommt die Decorator-Farbe.
- Inline-Templates in TypeScript (`template: \`<div>…</div>\``) sind ein
  String-Literal und bleiben komplett String-Farbe. Für Folien Templates
  lieber als eigenes HTML-Snippet zeigen.

Das Skript [`highlight_code.py`](../scripts/highlight_code.py) erkennt HTML
automatisch (Snippet beginnt mit `<` oder `@if`/`@for`/…); explizit per
`highlight(code, language="html")`.
