# Code-Slide Layout ("Code Window")

Für Code-Beispiele gibt es im **Angular HTTP**-Deck
(`1YQKMhSZvX_0PNBwvkUIpItLzhbrbOqXAIthOhjNKEAc`) ein eigenes Folienlayout
**"Code Window"** (aktuell `objectId: g13d90545163_0_305`, interner Name
weiterhin `BLANK` — Anzeigename ist das Relevante). Es enthält bereits die
komplette optische Hülle (Card mit Schatten, abgesetzte Tab-Kopfzeile,
farbiger Dot, Hintergrund-Farbverlauf) sowie drei fertige Platzhalter:

| Platzhalter-Typ | Verwendung                                  | Schrift (Default)        |
| --------------- | ------------------------------------------- | ------------------------ |
| `TITLE`         | Folientitel                                 | Arial 23pt               |
| `SUBTITLE`      | Folienkategorie                             | Helvetica, 10pt, #2563eb |
| `BODY`          | Code-Inhalt (siehe Abschnitt "Code")        | Fira Mono 13pt           |
| `BODY`          | Explanation (siehe Abschnitt "Hinweistext") | Helvetica 12pt           |

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

## Code

1. `createSlide` mit `slideLayoutReference: { layoutId: "<Code-Window-Explanation-objectId>" }`.
2. `get_page(presentationId, pageObjectId: "<neue Slide-ID>")` aufrufen, um die
   auf dieser Folie neu erzeugten Platzhalter-`objectId`s zu bekommen
   (erkennbar an `placeholder.type`: `TITLE`, `SUBTITLE`, `BODY`, `BODY`).
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

   Für HTML/Angular-Templates erkennt `highlight` die Sprache automatisch
   (Snippet beginnt mit `<` oder `@if`/`@for`/…); explizit mit
   `highlight(code, language="html")`. Token-Zuordnung: siehe
   [code-highlight-theme.md](./code-highlight-theme.md#html-angular-templates).

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

- Entnimm das Theme von [code-highlight-theme.md](./code-highlight-theme.md)

## Hinweistext (explanation)

### Card Container Specification

| Property             | Value                            | RGB (0–1)           | Hex      |
| :------------------- | :------------------------------- | :------------------ | :------- |
| Background Fill      | Light Warning Surface            | 0.996, 0.973, 0.965 | \#FEFAF6 |
| Border (Outer)       | 1px solid neutral                | 0.898, 0.906, 0.922 | \#E5E7EB |
| Accent Border (Left) | 4px solid alert red              | 0.851, 0.188, 0.145 | \#D93025 |
| Corner Radius        | 8px                              | \-                  | \-       |
| Padding              | 16px top/bottom, 20px left/right | \-                  | \-       |

---

### Typography & Color Specification

| Element                                                         | Font Family                           | Size  | Weight        | Color (Hex) | RGB (0–1)           | Special Styling                                                                                          |
| :-------------------------------------------------------------- | :------------------------------------ | :---- | :------------ | :---------- | :------------------ | :------------------------------------------------------------------------------------------------------- |
| Badge Label ("LIMITATION")                                      | Sans-Serif (Roboto / Google Sans)     | 11 pt | Bold (700)    | \#D93025    | 0.851, 0.188, 0.145 | Text Transform: UPPERCASE; Pill Fill: \#FCE8E6 (RGB: 0.988, 0.910, 0.902); Padding: 3px 8px; Radius: 4px |
| Section Title ("Constructor Injection")                         | Sans-Serif (Roboto / Google Sans)     | 18 pt | Bold (700)    | \#1F2937    | 0.122, 0.161, 0.216 | Margin-bottom: 8px                                                                                       |
| Body Description Text                                           | Sans-Serif (Roboto / Google Sans)     | 13 pt | Regular (400) | \#4B5563    | 0.294, 0.333, 0.388 | Line Height: 1.45                                                                                        |
| Inline Code Snippets (`@Service()`)                             | Monospace (Roboto Mono / Courier New) | 12 pt | Regular (400) | \#0080A0    | 0, 0.502, 0.627     | Uses Decorator color token from code palette                                                             |
| Fix Section Header ("💡 Recommended Fix")                       | Sans-Serif (Roboto / Google Sans)     | 14 pt | Bold (700)    | \#137333    | 0.075, 0.451, 0.200 | Includes lightbulb icon prefix (U+1F4A1); Margin-top: 12px                                               |
| Fix Description Text                                            | Sans-Serif (Roboto / Google Sans)     | 13 pt | Regular (400) | \#1F2937    | 0.122, 0.161, 0.216 | Line Height: 1.45                                                                                        |
| Fix Inline Code Snippet (`@Injectable({ providedIn: 'root' })`) | Monospace (Roboto Mono / Courier New) | 12 pt | Mixed         | Mixed       | Mixed               | `@Injectable` (\#0080A0), `providedIn` (\#2D60CA), `'root'` (\#0077AA)                                   |

---

### Layout Hierarchy

1.  Badge Pill ("LIMITATION") positioned at the top left of the card.
2.  Title ("Constructor Injection") directly below the badge.
3.  Problem Description paragraph below the title.
4.  Recommended Fix block separated by subtle divider or spacing, highlighted with green accent header.

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
