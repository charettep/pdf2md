# Usage Examples

## Quick Start

### Basic Conversion

Convert a PDF to Markdown with default settings:

```bash
python main.py ccq-1991.pdf
```

Output: `ccq-1991.md`

### With Custom Title

```bash
python main.py ccq-1991.pdf --title "CODE CIVIL DU QUÉBEC (CCQ-1991)"
```

### Save Both Raw Text and Markdown

```bash
python main.py ccq-1991.pdf --save-raw
```

This creates:
- `ccq-1991.md` (formatted markdown)
- `ccq-1991.txt` (raw extracted text)

### Custom Output Path

```bash
python main.py ccq-1991.pdf -o /mnt/shared/download/output.md
```

## Python API Usage

You can also use the package directly in Python:

```python
from pdf2md import PDFExtractor, MarkdownFormatter

# Extract text from PDF
extractor = PDFExtractor("ccq-1991.pdf")
raw_text = extractor.extract_text()

# Format to markdown
formatter = MarkdownFormatter(raw_text, document_title="CODE CIVIL DU QUÉBEC")
markdown = formatter.format_to_markdown()

# Save to file
with open("output.md", "w", encoding="utf-8") as f:
    f.write(markdown)
```

## Installation as Package

To install the package and use it anywhere:

```bash
pip install -e .
```

Then use it as a command:

```bash
pdf2md document.pdf -o output.md
```

## Output Sample

The generated markdown will have this structure:

```markdown
# CODE CIVIL DU QUÉBEC (CCQ-1991)
*À jour au 30 juin 2025*
*© Éditeur officiel du Québec*

---

## DISPOSITION PRÉLIMINAIRE

Le Code civil du Québec régit...

## LIVRE PREMIER

**DES PERSONNES**

### TITRE PREMIER

DE LA JOUISSANCE ET DE L'EXERCICE DES DROITS CIVILS

`Article 1`

#### CHAPITRE PREMIER

DE L'INTÉGRITÉ DE LA PERSONNE

##### SECTION I

**DES SOINS**

...
```

## Tested With

- **Document**: Code Civil du Québec (CCQ-1991)
- **Pages**: 554 pages
- **PDF Size**: 2.3 MB
- **Processing Time**: ~15 seconds
- **Output Size**: 1.5 MB markdown file
- **Lines Processed**: 28,816 lines

## Tips

1. **Large PDFs**: The tool handles large documents efficiently with progress indicators
2. **Encoding**: Uses UTF-8 encoding for proper French character support
3. **Structure**: Automatically detects hierarchical legal document structure
4. **Clean Output**: Removes page numbers and headers automatically
