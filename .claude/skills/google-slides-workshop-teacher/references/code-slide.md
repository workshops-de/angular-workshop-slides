# Code-Slide Layout ("Code Window")

Für Code-Beispiele gibt es im **Angular HTTP**-Deck
(`1YQKMhSZvX_0PNBwvkUIpItLzhbrbOqXAIthOhjNKEAc`) ein eigenes Folienlayout
**"Code Window"** (aktuell `objectId: g13d90545163_0_305`, interner Name
weiterhin `BLANK` — Anzeigename ist das Relevante). Es enthält bereits die
komplette optische Hülle (Card mit Schatten, abgesetzte Tab-Kopfzeile,
farbiger Dot, Hintergrund-Farbverlauf) sowie drei fertige Platzhalter:

| Platzhalter-Typ | Verwendung       | Schrift (Default)                 |
| --------------- | ---------------- | --------------------------------- |
| `TITLE`         | Folientitel      | Arial 23pt                        |
| `SUBTITLE`      | Dateiname im Tab | Roboto Mono 11pt, bold, `#434343` |
| `BODY`          | Code-Inhalt      | Fira Mono 13pt                    |

Da die Hülle jetzt Teil des Layouts ist, muss sie **nicht mehr pro Folie neu
gebaut werden** (kein manuelles Anlegen von Card/Divider/Dot/Hintergrund mehr
nötig). Neue Code-Folien einfach auf dieses Layout stellen und nur die drei
Platzhalter befüllen + das Syntax-Highlighting im Code-Platzhalter setzen.

Die Layout-`objectId` kann sich ändern, falls das Layout im Master neu
angelegt/dupliziert wird. Vor dem Bauen einer neuen Folie zur Sicherheit
gegenchecken:

```
get_presentation(presentationId, fields: "layouts(objectId,layoutProperties)")
→ Eintrag mit layoutProperties.displayName == "Code Window" suchen
```

## Bauablauf für eine neue Code-Folie

1. `createSlide` mit `slideLayoutReference: { layoutId: "<Code-Window-objectId>" }`.
2. `get_page(presentationId, pageObjectId: "<neue Slide-ID>")` aufrufen, um die
   auf dieser Folie neu erzeugten Platzhalter-`objectId`s zu bekommen
   (erkennbar an `placeholder.type`: `TITLE`, `SUBTITLE`, `BODY`).
3. Je Platzhalter: `insertText` mit dem gewünschten Inhalt (Titel, Dateiname,
   kompletter Codetext in einem Rutsch).
4. Auf dem `BODY`-Platzhalter das Syntax-Highlighting setzen (siehe unten) —
   zuerst ein `updateTextStyle` über `textRange.type: ALL` für Grundfarbe/Font/
   Size, danach gezielte `updateTextStyle`-Aufrufe mit
   `textRange.type: FIXED_RANGE` für jeden abweichenden Token.
5. **Indizes nie von Hand zählen.** Statt Token-Ranges manuell zu berechnen,
   das wiederverwendbare Highlighter-Skript
   [`scripts/highlight_code.py`](../scripts/highlight_code.py) nutzen:

   ```python
   import sys
   sys.path.insert(0, "<Pfad zu>/.claude/skills/google-slides-workshop-teacher/scripts")
   from highlight_code import highlight

   text, ranges = highlight(code, known_types=["BooksClient"])
   ```

   `code` ist der Codetext mit normalen `\n`-Zeilenumbrüchen; die Funktion
   gibt den fertigen Text (mit `` statt `\n`, siehe unten) und die
   Highlighting-Ranges zurück. `known_types` optional angeben für
   Klassennamen, die als bloße Referenz auftauchen (z. B. `inject(BooksClient)`),
   damit auch diese Vorkommen die Typen-Farbe bekommen. Das Skript ist ein
   Heuristik-basierter Tagger, kein echter Parser — nach dem Bauen die Folie
   trotzdem per `get_page` stichprobenartig gegenchecken.
6. Nach dem Bauen die Folie per `get_page` erneut auslesen und stichprobenartig
   prüfen, ob Ranges und Farben wie geplant angekommen sind.

### ⚠️ Zeilenumbrüche im Code: NIEMALS `\n`, IMMER ``

Ein normales `\n` (`insertText` mit "Enter") erzeugt in Google Slides einen
**neuen Absatz** — jede Codezeile bekommt dadurch den vollen Absatzabstand
(`spaceAbove`/`spaceBelow`) des Platzhalters, und der Code wirkt sichtbar
zu weit auseinandergezogen. Innerhalb eines Code-Blocks müssen die Zeilen
stattdessen durch einen **weichen Zeilenumbruch** (Shift+Enter in der UI,
technisch das Vertical-Tab-Zeichen ``) getrennt werden — das bleibt
im selben Absatz und hat keinen Absatzabstand.

- Beim Aufbau des Codetexts (egal ob im Python-Snippet aus Schritt 5 oder
  direkt im `insertText`-Aufruf) jede Zeile mit `` statt `\n`
  verbinden. Eine Leerzeile im Code ist einfach ``
  (zwei aufeinanderfolgende weiche Umbrüche).
- Da `` wie `\n` genau ein Zeichen ist, ändern sich dadurch **keine**
  Start-/End-Indizes der Highlighting-Ranges — 1:1 austauschbar.
- Kontrolle nach dem Bauen: `get_page` sollte im `BODY`-Platzhalter **einen
  einzigen** `paragraphMarker` zeigen, der den kompletten Text umspannt
  (nicht einen `paragraphMarker` pro Zeile). Tauchen mehrere
  `paragraphMarker`-Einträge auf, wurde versehentlich `\n` verwendet — Text
  löschen (`deleteText`, `textRange.type: ALL`) und mit `` neu
  einfügen.
- Nur TITLE und SUBTITLE (einzeilig) nutzen normales `insertText` ohne diese
  Sonderbehandlung.

## Syntax-Highlighting im Code (`BODY`-Platzhalter)

Blau-lastige Basispalette, passend zum Akzent des Layouts:

| Token-Art                                                                                                         | Farbe (RGB 0–1)       | Hex       | Bold |
| ----------------------------------------------------------------------------------------------------------------- | --------------------- | --------- | ---- |
| Keywords (`export`, `class`… `private`, `return`, `this`, `import`, `from`)                                       | `0, 0.0627, 0.502`    | `#001080` | ja   |
| Decorator (`@Injectable`, `@Component` …)                                                                         | `0.357, 0.576, 0.902` | `#5B93E6` | nein |
| Typen / Methodennamen / Funktionsaufrufe (Klassen, `getAll`, `get`, `inject`, generische Typparameter wie `Book`) | `0.176, 0.376, 0.792` | `#2D60CA` | nein |
| String-Literale                                                                                                   | `0, 0.467, 0.667`     | `#0077AA` | nein |
| Standardtext (Interpunktion, Operatoren, restlicher Code)                                                         | `0.2, 0.2, 0.2`       | `#333333` | nein |

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

## Referenzfolie

Live-Beispiel mit bereits gesetztem Highlighting: Folie `wsde01_slide`
(`https://docs.google.com/presentation/d/1YQKMhSZvX_0PNBwvkUIpItLzhbrbOqXAIthOhjNKEAc/edit#slide=id.wsde01_slide`).
Bei Unsicherheit dort per `get_page` die exakten Werte gegenchecken, statt zu
raten — diese Folie nutzt allerdings noch die alte, manuell gebaute Hülle
(vor Einführung des "Code Window"-Layouts).

## Hinweis für Layout-Pflege (nicht Teil des normalen Workflows)

Das Layout selbst nutzt für die Tab-Kopfzeile den Shape-Typ
`ROUND_2_SAME_RECTANGLE` (rundet nur zwei benachbarte Ecken) — das löst das
Problem, dass die Slides API bei normalen Rechtecken keine einseitig
gerundeten Ecken erlaubt. Die Card hat zusätzlich einen echten Slides-Schatten
(`shadow.propertyState: RENDERED`, kein `NOT_RENDERED`). Änderungen an dieser
Hülle passieren im Master (_Folie → Master bearbeiten_), nicht mehr über
API-Calls pro Folie.
