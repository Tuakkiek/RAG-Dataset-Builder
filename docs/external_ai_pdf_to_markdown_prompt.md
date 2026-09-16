# Prompt: PDF to Markdown Compatible with RAG Dataset Pipeline

Copy the prompt below and attach the PDF.

---

## Role

You are a document digitization system. Convert the attached PDF into one faithful Markdown document for a RAG dataset. Preserve the source content, reading order, page boundaries, printed page numbers, headings, formulas, tables, lists, figures, captions, metadata, references, and code.

Do not summarize, rewrite, translate, correct, or omit content.

## Output

Return exactly one Markdown document and nothing else:

- Do not wrap the result in a Markdown code fence.
- Do not add an explanation before or after the document.
- Use UTF-8 and preserve Vietnamese diacritics and original symbols.
- Keep the original reading order: top to bottom, left to right, and column by column for multi-column pages.
- Separate logical blocks with one blank line.

## Mandatory page marker

Before the first content block belonging to each PDF page, emit exactly one marker:

<!-- page: N -->

`N` is a positive integer.

The marker rules are:

1. If a printed page number is visible and readable on the page, use that number for `N`.
2. Printed numbering may start at any value, including 0, 165, or another value. Preserve it exactly when it is readable.
3. If the printed number is not visible on a page but a reliable sequence has already been established, infer the missing number from that sequence and continue it.
4. Pages before the first readable printed page number may be unnumbered front matter. For those pages, use generated one-based numbering according to their physical PDF position. Do not invent a printed number such as 164 merely because the first readable page is 165.
5. If no printed page number can be identified anywhere in the PDF, use generated one-based numbering from 1 to the number of PDF pages.
6. Never use `page: 0` in a marker.
7. Use one marker per physical PDF page, even if that page contains no extractable text. For an empty page, place the marker alone.
8. Do not confuse the PDF physical position with the printed page number. The first PDF page is physical page 1, but its logical printed page may be different or absent.

Example for a document with two unnumbered front-matter pages followed by printed page 165:

<!-- page: 1 -->

Front matter...

<!-- page: 2 -->

Preface...

<!-- page: 165 -->

Main content...

<!-- page: 166 -->

Next page...

## Text extraction

Extract all readable text, including:

- title, authors, affiliations, dates, abstracts, keywords, and metadata;
- headings and subheadings;
- paragraphs and continuation paragraphs across page boundaries;
- ordered and unordered lists;
- captions and footnotes;
- references and appendices;
- headers and footers only when they are meaningful document content.

Do not duplicate repeated running headers or footers on every page. If a header/footer carries a meaningful page number, use it to determine the page marker, but do not repeat it as body content unless it is part of the document.

Preserve paragraph boundaries. Do not merge unrelated blocks. If a paragraph continues across pages, keep the page marker between the portions and preserve the text in reading order.

## Headings

Represent headings using Markdown ATX headings:

- `#` for the document title or top-level heading;
- `##` for a section;
- `###` for a subsection;
- `####` and deeper levels when clearly present in the source.

Do not promote ordinary large text, running headers, author names, or captions to headings unless the source structure clearly indicates that they are headings.

## Lists

Preserve list structure:

- unordered items: `- item`;
- ordered items: `1. item`.

Keep nested list indentation when it is visible. Do not flatten a list into a paragraph.

## Tables

Reconstruct tables as Markdown tables whenever the row and column structure is readable:

| Column 1 | Column 2 |
| -------- | -------- |
| value 1  | value 2  |

Rules:

- preserve headers, rows, column order, and cell text;
- preserve empty cells;
- escape a literal pipe inside a cell as `\\|`;
- do not silently drop a row or column;
- if the table cannot be reconstructed reliably, preserve its text in reading order and label the limitation with a short HTML comment, for example `<!-- table structure uncertain on page N -->`.

## Formulas

Convert mathematical formulas to valid LaTeX:

- inline formula: `$...$`;
- display formula: `$$` on its own line, then the LaTeX, then `$$` on its own line.

Rules:

- preserve mathematical meaning and equation numbering when visible;
- use standard LaTeX commands such as `\\alpha`, `\\frac`, `\\sum`, `\\left`, and `\\right`;
- do not output raw Unicode math glyphs when they replace an unreadable formula;
- escape backslashes correctly for the final Markdown text;
- do not add extra `$` or `$$` delimiters around an already delimited formula.

Example:

$$
\\mathrm{Precision} = \\frac{TP}{TP + FP}
$$

## Images and figures

For every meaningful embedded figure or image:

1. preserve its position in the reading order;
2. preserve the caption immediately near it;
3. use a stable placeholder when the image file cannot be exported:

`![Figure: fig-<physical-page>-<sequence>]`

Do not fabricate visual details that cannot be read. If the image contains essential text, transcribe that text as a paragraph or caption near the placeholder.

## Code and pseudocode

Preserve code as fenced blocks and identify the language when it is clear:

```python
def example(value):
    return value + 1
```

Do not reformat code in a way that changes its meaning.

## OCR and uncertainty

When the PDF is scanned or text is unclear:

- inspect the page image rather than guessing from incomplete text extraction;
- preserve all characters that can be read;
- never silently invent missing words, numbers, formulas, or page numbers;
- when a small part is genuinely unreadable, use `[unclear]` in that exact location;
- keep the rest of the page in the correct order.

## Final validation before returning

Check all of the following:

1. The output is one Markdown document with no outer code fence.
2. There is exactly one `<!-- page: N -->` marker for every physical PDF page.
3. Every marker uses a positive integer.
4. Printed page numbers are preserved whenever readable.
5. A printed start number such as 165 is not changed to 1.
6. Unnumbered front matter is not assigned a fabricated preceding printed number.
7. Headings, lists, tables, formulas, captions, references, and code remain structurally identifiable.
8. Formula delimiters and code fences are balanced.
9. No content was summarized, translated, or omitted intentionally.
10. The document is suitable for downstream parsing by a system that recognizes `<!-- page: N -->`.

Return only the final Markdown document.

---

## Optional comparison metadata

If the caller explicitly asks for an audit report in addition to the Markdown, return it separately after the Markdown under a clearly delimited section named `AUDIT_REPORT`. Otherwise, do not include any audit report in the Markdown output.

The audit report should state:

- total physical PDF pages;
- detected printed-page range, if any;
- whether numbering was detected or generated;
- pages with uncertain OCR, tables, formulas, or figures;
- pages where the printed number was inferred rather than directly read.
