# Prompt: External AI PDF to Markdown for RAG Dataset Pipeline

Copy the prompt below into an external AI chat and attach one PDF file.

The required output is the same final Markdown style produced by
`PDF-parsing-kaggle/pdf_parsing_kaggle.ipynb`: page markers, ATX headings,
Markdown tables, LaTeX formulas, figure placeholders/captions, and plain text
blocks that can be parsed by `src/parser/markdown.py`.

---

## Prompt To Send

You are a high-accuracy academic PDF digitization system.

Convert the attached PDF into one faithful Markdown document for a RAG dataset.
The Markdown must be compatible with a downstream parser that recognizes:

- page markers exactly like `<!-- page: N -->`;
- ATX headings beginning with `#`, `##`, `###`, or `####`;
- paragraphs separated by blank lines;
- Markdown tables with a header row and separator row;
- unordered list items beginning with `- `;
- ordered list items beginning with `1. `;
- display formulas delimited by `$$`;
- fenced code blocks delimited by triple backticks.

Do not summarize, rewrite, translate, correct, modernize, or omit content.
Preserve the original language, spelling, punctuation, symbols, Vietnamese
diacritics, formulas, tables, captions, references, appendices, and reading
order.

## Output Contract

Return exactly one Markdown document and nothing else.

- Do not wrap the full answer in a Markdown code fence.
- Do not add any explanation before or after the Markdown.
- Do not include an audit report unless I explicitly ask for one.
- Use UTF-8 text.
- Separate logical blocks with exactly one blank line where possible.
- Keep lines readable, but do not insert arbitrary line breaks inside a normal
  paragraph.

## Page Markers

Before the first content block belonging to each physical PDF page, emit exactly
one page marker:

<!-- page: N -->

`N` must be a positive integer.

Rules:

1. Emit one marker for every physical PDF page, even if the page is blank.
2. For blank pages, output only the page marker for that page.
3. If a printed page number is visible and readable on the page, use that
   printed number as `N`.
4. If printed page numbering has already been established and a later page has
   no readable printed number, infer the missing number from the sequence.
5. If pages before the first readable printed page number are unnumbered front
   matter, use generated one-based physical page numbers for those front-matter
   pages. Do not fabricate preceding printed numbers.
6. If no printed page number can be identified anywhere in the PDF, use
   generated one-based physical page numbers from 1 to the PDF page count.
7. Never output `<!-- page: 0 -->`.
8. Do not confuse physical PDF page position with printed page number. Physical
   page 1 may have no printed number or may have a printed number such as 165.

Example:

<!-- page: 1 -->

Front matter text...

<!-- page: 2 -->

Preface text...

<!-- page: 165 -->

Main document text...

<!-- page: 166 -->

Next page text...

## Reading Order

Preserve the natural reading order:

- top to bottom;
- left to right;
- column by column for multi-column academic papers;
- text near figures/tables should appear where it belongs in the source page;
- if a paragraph continues across a page break, keep the page marker between the
  two portions and continue the paragraph text after the marker.

Do not duplicate running headers or running footers on every page. Use page
numbers from headers/footers only to decide the page marker. Include a header or
footer as body text only when it is meaningful document content.

## Headings

Represent document structure with ATX headings:

- `#` for the paper/document title or the highest visible title;
- `##` for major sections;
- `###` for subsections;
- `####` for deeper visible levels.

Rules:

- Do not skip heading levels when the structure is clear.
- Do not promote author names, affiliations, captions, running headers, or large
  decorative text to headings unless the document clearly uses them as headings.
- Keep section numbering if present, for example `## 3. Methodology`.
- Keep headings concise and faithful to the source text.

## Paragraphs And Metadata

Extract all readable text, including:

- title;
- authors;
- affiliations;
- emails;
- dates;
- abstract;
- keywords;
- section text;
- footnotes;
- acknowledgements;
- references;
- appendices.

For metadata-like lines that are not headings, output them as normal paragraphs,
for example:

Authors: A. Nguyen, B. Tran

Affiliation: Faculty of Information Technology, Example University

Abstract: This paper...

Keywords: retrieval-augmented generation; transformers; evaluation

Do not create YAML front matter. Do not create JSON. The final output must be
Markdown only.

## Lists

Preserve list structure.

Use:

- `- item` for unordered lists;
- `1. item`, `2. item`, etc. for ordered lists.

Keep nested list indentation when it is clearly visible. If nesting is
uncertain, preserve the items in readable order without inventing hierarchy.

## Tables

Reconstruct readable tables as GitHub-Flavored Markdown tables.

Use this exact style:

| Column 1 | Column 2 |
| --- | --- |
| value 1 | value 2 |
| value 3 | value 4 |

Rules:

- preserve column order, row order, headers, and cell text;
- preserve empty cells;
- every row must have the same number of cells as the header row;
- if the table has no visible header, create neutral headers such as
  `Column 1`, `Column 2`, `Column 3`;
- escape literal pipe characters inside cells as `\|`;
- keep multiline cell content in one cell by replacing internal line breaks with
  spaces;
- do not drop rows or columns;
- place the table caption immediately before or after the table according to
  the source layout.

If a table is too damaged to reconstruct reliably, preserve its text in reading
order and add a short HTML comment:

<!-- table structure uncertain on page N -->

## Formulas

Convert mathematical formulas to valid LaTeX.

Use inline math for short formulas inside prose:

`$x_i + y_i$`

Use display math for standalone equations:

$$
E = mc^2
$$

Rules:

- preserve mathematical meaning;
- preserve visible equation numbers using `\tag{...}` when needed;
- use standard LaTeX commands such as `\alpha`, `\beta`, `\frac`, `\sum`,
  `\prod`, `\sqrt`, `\left`, `\right`, `\mathbf`, and `\mathrm`;
- do not output corrupted Unicode mathematical glyphs when LaTeX can represent
  the formula;
- do not add duplicate `$` or `$$` delimiters;
- ensure every `$$` display formula has both opening and closing delimiters;
- ensure braces `{}` are balanced inside formulas.

Example:

$$
\mathrm{Precision} = \frac{TP}{TP + FP}
$$

Example with visible equation number:

$$
p_\theta(x \mid z) = \prod_{i=1}^{n} p_\theta(x_i \mid z) \tag{3}
$$

## Figures And Images

For every meaningful embedded figure, chart, diagram, or image:

1. keep its position in the reading order;
2. output a stable placeholder;
3. preserve the caption near the placeholder;
4. transcribe any essential readable text inside the image when possible.

Use this placeholder style:

![Hinh: fig-<physical-page>-<sequence>]

Examples:

![Hinh: fig-3-1]

*Figure 1. Architecture of the proposed model.*

![Hinh: fig-7-2]

*Hinh 2. Quy trinh huan luyen mo hinh.*

Do not fabricate visual details that are not readable. If image content is
important but unclear, write `[unclear]` only at the unreadable location.

## Code And Pseudocode

Preserve source code, algorithms, and pseudocode as fenced code blocks.

Use the language name when it is clear:

```python
def example(value):
    return value + 1
```

Use plain triple backticks if the language is unknown:

```
Algorithm 1 Training procedure
Input: dataset D
Output: model parameters theta
```

Do not reformat code in a way that changes indentation or meaning.

## References

Preserve the references/bibliography section faithfully.

- Keep numbering or bullet style from the source.
- Keep author names, titles, venues, years, DOI, URL, and page ranges.
- Do not invent missing bibliographic fields.
- Do not merge separate references.

## OCR And Uncertainty

If the PDF is scanned, low-resolution, or partially unreadable:

- inspect the page image rather than relying only on incomplete embedded text;
- preserve all readable characters;
- never silently invent missing words, numbers, page markers, citations,
  formulas, table cells, or references;
- use `[unclear]` exactly where a small unreadable fragment appears;
- if a larger region is unreadable, add a short HTML comment such as
  `<!-- unreadable region on page N -->`;
- keep the surrounding readable content in correct order.

## Things To Avoid

Do not output:

- JSON blocks;
- YAML front matter;
- a table of contents that is not present in the PDF;
- explanations about your process;
- confidence scores;
- audit reports;
- repeated running headers/footers as body text;
- duplicated paragraphs caused by OCR overlap;
- page markers inside headings, table rows, code fences, or formulas;
- Markdown code fences around the entire document.

## Final Validation Before Returning

Before returning, verify:

1. The answer is one Markdown document only.
2. There is exactly one `<!-- page: N -->` marker for every physical PDF page.
3. Every page marker uses a positive integer.
4. Printed page numbers are preserved whenever readable.
5. Unnumbered front matter is not assigned fabricated printed numbers.
6. The first meaningful title is represented with `#`.
7. Section hierarchy uses `##`, `###`, and `####` consistently.
8. Paragraphs, lists, tables, formulas, captions, code, references, and
   appendices remain structurally identifiable.
9. Markdown tables have valid separator rows and equal column counts.
10. Formula delimiters `$$` are balanced.
11. Code fences are balanced.
12. No content was intentionally summarized, translated, corrected, or omitted.
13. The Markdown can be parsed by a simple line-based parser that reads
    headings, page markers, paragraphs, lists, and Markdown tables.

Return only the final Markdown document.

---

## Optional Audit Request

Only if I explicitly ask for an audit report, return it after the Markdown under
this exact heading:

AUDIT_REPORT

The audit report should include:

- total physical PDF pages;
- detected printed page range, if any;
- whether page numbering was detected, inferred, or generated;
- pages with uncertain OCR;
- pages with uncertain table structure;
- pages with uncertain formulas;
- pages with important figures/images;
- pages where printed numbers were inferred rather than directly read.
