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
