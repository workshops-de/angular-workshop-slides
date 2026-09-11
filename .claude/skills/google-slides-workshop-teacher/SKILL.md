---
name: google-slides-workshop-teacher
description: Sichert Aktualisierungen der Workshop-Folien in Google Slides ab, bevor sie freigegeben werden. Fragt nach der betroffenen Präsentation und einer kurzen Beschreibung der inhaltlichen Änderung, durchsucht die Folien per Google Slides MCP nach passenden Treffern, bietet direkte Deep-Links zu den Kandidaten-Folien zur Scope-Prüfung an und fragt abschließend kurz, ob das 4-MAT-Lernprinzip berücksichtigt wurde. Auslöser: "Slides aktualisieren", "Slide-Update prüfen", "Folien absichern", "Google Slides Review", "hat sich was an den Folien geändert".
---

# Vorbedingung

Bevor du etwas an den [Lessons](../../../lessons/) veränderst musst du `git submodule update sample-solution` ausführen und sicherstellen, dass die Musterlösung im `solution`-Branch aktuell ist.

# Google Slides Workshop Teacher

Review-Workflow für Änderungen an den Google-Slides-Präsentationen des Angular
Workshops. Nutzt ausschließlich die Google Slides MCP-Tools
(`get_presentation`, `summarize_presentation`, `get_page`) — keine eigene
Driver-Software nötig, da die Präsentationen direkt über MCP ansteuerbar sind.

## Bekannte Präsentationen

| Präsentation         | ID                                              |
| -------------------- | ----------------------------------------------- |
| Angular Basics       | `1KJMDvEUIWDHluMPLffiBnadVSO2IElTAs7jPsMadehw`  |
| Angular HTTP         | `1YQKMhSZvX_0PNBwvkUIpItLzhbrbOqXAIthOhjNKEAc`  |
| Angular Routing      | `193jtyGRGHGKr7gwHP-jWj8IcENWggzpPClVxmFgPAkY`  |
| Angular Testing      | `1zRNyaH3lcOhChTl4VIetlSV8WScYLzxvzZ3Mx8zp8xA`  |
| Angular Signal Forms | `1DLlkWJBHaFRXL0tUaj83I19IQg5tJJk8DjK8ZhNvv1I`  |
| Angular Vitest       | `1PHpUoQmxuujWJ9pq-DHX4B27qZreWXZ4btqlAIXwrkc/` |

## Ablauf

1. **Präsentation klären.** Wenn der Nutzer sie nicht schon genannt hat: nach
   der betroffenen Präsentation aus obiger Tabelle fragen (per
   `AskUserQuestion`, Optionen = die vier Namen).

2. **Änderung klären.** Kurz erfragen, was sich inhaltlich am Lesson-Content
   geändert hat (Thema, Stichworte, neuer/entfernter Abschnitt). Das ist die
   Grundlage für die Scope-Suche — ohne Beschreibung keine sinnvolle
   Eingrenzung möglich.

3. **Folien durchsuchen.**
   `summarize_presentation(presentationId, include_notes: true)` aufrufen.
   Das liefert pro Folie `slideNumber`, `slideId` und den vollständigen
   Text-Content (inkl. Sprechernotizen). Die vom Nutzer genannten
   Stichworte/Themen gegen diesen Text abgleichen (Titel, Bulletpoints,
   Notizen) und eine Kandidatenliste der thematisch passenden Folien
   erstellen — lieber zu breit als zu eng, die endgültige Eingrenzung macht
   der Nutzer in Schritt 4.

4. **Kandidaten mit Links vorlegen.** Für jede Kandidaten-Folie einen
   Deep-Link im Format
   `https://docs.google.com/presentation/d/<presentationId>/edit#slide=id.<slideId>`
   ausgeben, zusammen mit Foliennummer und einem kurzen Auszug (Titel oder
   erste Zeile), damit der Nutzer ohne Klicken schon grob einschätzen kann.
   Den Nutzer fragen, welche der Kandidaten tatsächlich im Scope der
   Aktualisierung liegen (z. B. mit `AskUserQuestion`,
   `multiSelect: true`, Optionen = die Kandidatenfolien).

5. **4-MAT-Check.** Für die bestätigten Folien kurz nachfragen, ob bei der
   Aktualisierung das 4-MAT-Lernprinzip berücksichtigt wurde — also ob der
   Inhalt die vier Phasen abdeckt:
   - **Warum** (Motivation/Kontext, warum ist das relevant)
   - **Was** (die eigentlichen Fakten/Konzepte)
   - **Wie** (praktische Anwendung/Übung)
   - **Was-wäre-wenn** (Transfer, Varianten, offene Fragen)

   Das ist eine reflektierende Rückfrage an den Nutzer (z. B. per
   `AskUserQuestion`, Ja/Nein/Teilweise) — kein automatischer Contentcheck,
   da 4-MAT nicht aus dem reinen Folientext ableitbar ist.

   Wenn du selbst erkennst dass kein 4-MAT vorliegt, empfehle nützliche Ergänzungen.

6. **Kurzes Fazit.** Am Ende in 2–3 Sätzen zusammenfassen: welche Folien als
   im Scope bestätigt wurden (mit Links), und das Ergebnis der
   4-MAT-Rückfrage. Keine Änderungen an den Slides selbst vornehmen, sofern
   nicht explizit verlangt.

7. **Umsetzung** Anspassen bestehende und/oder Erstellen neuer Slides

- Neue Slides sollen immer auf English sein.
- Erstelle dazu im Didaktischen Konzept jeweils Slides die folgende Fragen beantworten:
  - Titel des Kapitels/Themas (Layout: Abschnittüberschrift)
  - Little What (Kurze Erklärung, Ein Satz der das Zusammen fasst. Layout: Little What)
  - Why (Warum brauchen wir dieses Feature. Layout: Why 1)
  - How (Wie nutzen wir es)
  - What (Beispiele wir wir es nutzen)
  - Task (Titel der Aufgabe wie im GitHub Issue. Layout: Task)
  - What if? (Edgecased die ggf. behandelt werden)

Wenn du Aufzählungen nutzt, schau das du nicht mehr als 4 Punkte nutzt und jeder Punkt maximal 70 Zeichen hat. Sonst passt es nicht auf die Slide.

Achte bei Code-Beispielen darauf, dass diese mit dem in den Code-Slides vorhandenem Syntax-Highlighting ausgezeichnet sind.

Die Titel der Slides sollen kurz und einzeilig sein.

## Hinweise

- `get_page(presentationId, pageObjectId)` liefert Detaildaten zu genau
  einer Folie, falls der Summary-Auszug für die Einschätzung nicht reicht.
- Die Slide-IDs aus `summarize_presentation` sind identisch mit den
  `pageObjectId`-Werten für `get_page` und mit dem `id.<slideId>`-Teil im
  Deep-Link.
- Dieser Skill ändert nichts an den Präsentationen — er ist reine
  Review-/Absicherungs-Hilfe vor einer manuellen oder separat beauftragten
  Aktualisierung.
- Die Sprache der Slides ist Englisch. Bei allen inhaltlichen Vorschlägen,
  Formulierungshilfen oder Textänderungen für die Slides selbst ist Englisch
  beizubehalten — nur die Kommunikation mit dem Nutzer in diesem Skill läuft
  auf Deutsch.
