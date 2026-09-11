"""
Syntax highlighter for the "Code Window" slide layout's BODY placeholder.

Given TypeScript/Angular-template-ish code (lines joined with plain "\n"),
computes:
  - the text to insert, with "\n" replaced by "\x0b" (vertical tab / soft
    line break) so Slides doesn't add per-line paragraph spacing
  - a list of {start, end, color, bold} ranges matching the palette in
    references/code-slide.md, ready to feed into updateTextStyle
    FIXED_RANGE requests

Usage as a library:
    from highlight_code import highlight
    text, ranges = highlight(code, known_types=["BooksClient"])

Usage as a CLI (reads code from stdin, prints {"text":..., "ranges":...}):
    python3 highlight_code.py < snippet.ts

known_types: pass class/interface names that appear as bare references
(e.g. inside inject(...) calls) elsewhere in the snippet, so every
occurrence gets the TYPE color even where it isn't followed by "(" or
after class/extends/implements.

This covers common TypeScript/Angular syntax well but is a heuristic, not
a real parser — always spot-check the built slide with get_page afterwards.
"""

import re
import json

KEYWORD = {"red": 0, "green": 0.0627, "blue": 0.502}
DECORATOR = {"red": 0, "green": 0.502, "blue": 0.627}
TYPE = {"red": 0.176, "green": 0.376, "blue": 0.792}
STRING = {"red": 0, "green": 0.467, "blue": 0.667}
DEFAULT = {"red": 0.2, "green": 0.2, "blue": 0.2}
COMMENT = {"red": 0.6, "green": 0.6, "blue": 0.6}

KEYWORDS = set("""export class private public protected return this import from readonly
async await const let var new extends implements interface static void true false null
undefined function if else for while try catch finally throw typeof instanceof in of
get set default case switch break continue delete yield as""".split())


def highlight(code_nl, known_types=None):
    """code_nl: text using "\\n" between lines. Returns (text_with_vt, ranges)."""
    text = code_nl.replace("\n", "\x0b")
    n = len(text)
    style = [None] * n

    def mark(a, b, key, bold=False):
        for i in range(a, b):
            if style[i] is None:
                style[i] = (key, bold)

    # comments (// to end of physical line, i.e. until \x0b or end)
    for m in re.finditer(r'//[^\x0b]*', text):
        mark(m.start(), m.end(), "COMMENT")

    # strings (single, double, backtick) - not touching already-marked spans
    for m in re.finditer(r"""'(?:[^'\\]|\\.)*'|"(?:[^"\\]|\\.)*"|`(?:[^`\\]|\\.)*`""", text):
        a, b = m.span()
        if style[a] is None:
            mark(a, b, "STRING")

    # decorators / Angular control-flow (@Component, @for, @if, ...)
    for m in re.finditer(r'@[A-Za-z_][A-Za-z0-9_]*', text):
        a, b = m.span()
        if style[a] is None:
            mark(a + 1, b, "DECORATOR")  # color the name only, not the @

    # class/interface/extends/implements NAME -> TYPE
    for m in re.finditer(r'\b(class|interface|extends|implements)\s+([A-Za-z_][A-Za-z0-9_]*)', text):
        a, b = m.span(2)
        if style[a] is None:
            mark(a, b, "TYPE")

    # generic type params <Ident> and array types Ident[]
    for m in re.finditer(r'<([A-Za-z_][A-Za-z0-9_]*)\s*(?:\[\])?>', text):
        a, b = m.span(1)
        if style[a] is None:
            mark(a, b, "TYPE")
    for m in re.finditer(r'\b([A-Z][A-Za-z0-9_]*)\[\]', text):
        a, b = m.span(1)
        if style[a] is None:
            mark(a, b, "TYPE")

    # type annotations: ": Ident" (colon-space-capitalized identifier)
    for m in re.finditer(r':\s*([A-Z][A-Za-z0-9_]*)\b', text):
        a, b = m.span(1)
        if style[a] is None:
            mark(a, b, "TYPE")

    # identifier( -> TYPE (method/function call or decl), excluding keywords
    for m in re.finditer(r'\b([A-Za-z_][A-Za-z0-9_]*)\s*(?=\()', text):
        name = m.group(1)
        a, b = m.span(1)
        if name in KEYWORDS:
            continue
        if style[a] is None:
            mark(a, b, "TYPE")

    # known extra type names (bare references, e.g. inject(BooksClient))
    if known_types:
        for tname in known_types:
            for m in re.finditer(r'\b' + re.escape(tname) + r'\b', text):
                a, b = m.span()
                if style[a] is None:
                    mark(a, b, "TYPE")

    # keywords (word boundary), only over unmarked spans
    for m in re.finditer(r'\b[A-Za-z_][A-Za-z0-9_]*\b', text):
        w = m.group(0)
        a, b = m.span()
        if w in KEYWORDS and style[a] is None:
            mark(a, b, "KEYWORD", bold=True)

    colors = {"KEYWORD": KEYWORD, "DECORATOR": DECORATOR, "TYPE": TYPE, "STRING": STRING, "COMMENT": COMMENT}
    ranges = []
    i = 0
    while i < n:
        if style[i] is None:
            i += 1
            continue
        key, bold = style[i]
        j = i
        while j < n and style[j] == (key, bold):
            j += 1
        ranges.append({"start": i, "end": j, "color": colors[key], "bold": bold})
        i = j

    return text, ranges


if __name__ == "__main__":
    import sys
    code = sys.stdin.read()
    text, ranges = highlight(code)
    print(json.dumps({"text": text, "ranges": ranges}, indent=2))
