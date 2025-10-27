# PDF to Markdown Converter for Legal Documents

A Python application that extracts text from PDF files and converts them to well-structured Markdown format, optimized for legal documents such as the Quebec Civil Code (Code Civil du Québec).

## Features

- **High-Quality Text Extraction**: Uses PyMuPDF for accurate text extraction from PDF files
- **Intelligent Structure Detection**: Automatically detects and formats hierarchical document structures:
  - Books (LIVRE)
  - Titles (TITRE)
  - Chapters (CHAPITRE)
  - Sections (SECTION)
  - Subsections (§)
  - Articles and legal references
- **Clean Output**: Removes page headers/footers and other metadata
- **Command-Line Interface**: Easy-to-use CLI for batch processing
- **Customizable**: Support for different document titles and output paths

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or install the package:

```bash
pip install -e .
```

## Usage

### Basic Usage

Convert a PDF to Markdown:

```bash
python main.py ccq-1991.pdf
```

This will create `ccq-1991.md` in the same directory.

### Sample Files

The `samples/` folder contains example files demonstrating the converter's capabilities:
- **ccq-1991.pdf**: Original Quebec Civil Code PDF (2.3 MB, 554 pages)
- **ccq-1991_pymupdf.txt**: Raw text extraction using PyMuPDF
- **ccq-1991_pypdf2.txt**: Raw text extraction using PyPDF2 (for comparison)
- **ccq-1991-test.md**: Final formatted Markdown output (1.5 MB, 28,816 lines)

### Specify Output File

```bash
python main.py input.pdf -o output.md
```

### Custom Document Title

```bash
python main.py document.pdf --title "CODE CIVIL DU QUÉBEC (CCQ-1991)"
```

### Save Raw Text

Save both the raw extracted text and the formatted markdown:

```bash
python main.py document.pdf --save-raw
```

This creates:
- `document.md` (formatted markdown)
- `document.txt` (raw extracted text)

### Command-Line Options

```
usage: main.py [-h] [-o OUTPUT_MD] [-t TITLE] [--save-raw] [-v] input_pdf

Convert PDF legal documents to structured Markdown format

positional arguments:
  input_pdf             Path to input PDF file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_MD, --output OUTPUT_MD
                        Output markdown file path (default: input filename with .md extension)
  -t TITLE, --title TITLE
                        Document title for the markdown file (default: extracted from filename)
  --save-raw            Save raw extracted text to .txt file
  -v, --version         show program's version number and exit

Examples:
  main.py document.pdf                    # Creates document.md
  main.py document.pdf -o output.md       # Specify output file
  main.py document.pdf --title "My Doc"   # Custom document title
  main.py document.pdf --save-raw         # Also save raw text extraction
```

### Python API Usage

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

### Installation as Package

To install the package and use it anywhere:

```bash
pip install -e .
```

Then use it as a command:

```bash
pdf2md document.pdf -o output.md
```

## Project Structure

```
pdf2md/
├── pdf2md/                    # Main package
│   ├── __init__.py           # Package initialization
│   ├── extractor.py          # PDF text extraction (PyMuPDF)
│   ├── formatter.py          # Markdown formatting logic
│   └── cli.py                # Command-line interface
├── samples/                   # Sample files demonstrating usage
│   ├── ccq-1991.pdf          # Sample PDF input (Quebec Civil Code)
│   ├── ccq-1991_pymupdf.txt  # Raw text extraction (PyMuPDF)
│   ├── ccq-1991_pypdf2.txt   # Raw text extraction (PyPDF2)
│   └── ccq-1991-test.md      # Final Markdown output
├── examples/                  # Additional example outputs
├── requirements.txt          # Dependencies
├── setup.py                  # Package configuration
├── README.md                 # This file
└── main.py                   # Entry point script
```

## How It Works

### 1. Text Extraction

The `PDFExtractor` class uses PyMuPDF to extract text from PDF files page by page:

```python
from pdf2md import PDFExtractor

extractor = PDFExtractor("document.pdf")
raw_text = extractor.extract_text()
```

### 2. Markdown Formatting

The `MarkdownFormatter` class applies intelligent formatting rules to structure the text:

```python
from pdf2md import MarkdownFormatter

formatter = MarkdownFormatter(raw_text, document_title="My Document")
markdown = formatter.format_to_markdown()
```

### 3. Structure Detection

The formatter detects and applies appropriate markdown headings:

| Document Element | Markdown Level | Example |
|-----------------|---------------|---------|
| LIVRE (Book) | `##` | `## LIVRE PREMIER` |
| TITRE (Title) | `###` | `### TITRE PREMIER` |
| CHAPITRE (Chapter) | `####` | `#### CHAPITRE PREMIER` |
| SECTION | `#####` | `##### SECTION I` |
| § (Subsection) | `######` | `###### § 1. —` |
| Articles | Inline code | `` `Article 50` `` |
| Legal references | Italics | `*1991, c. 64, a. 123*` |

## Example Output

Input PDF: `ccq-1991.pdf` (Code Civil du Québec)

Output Markdown structure:
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

### TITRE DEUXIÈME

**DE CERTAINS DROITS DE LA PERSONNALITÉ**

#### CHAPITRE PREMIER

DE L'INTÉGRITÉ DE LA PERSONNE

##### SECTION I

**DES SOINS**
...
```

## Dependencies

- **PyMuPDF** (≥1.23.0): High-quality PDF text extraction
- **PyPDF2** (≥3.0.0): Alternative PDF library (for reference)

## Tested With

- **Document**: Code Civil du Québec (CCQ-1991)
- **Pages**: 554 pages
- **PDF Size**: 2.3 MB
- **Processing Time**: ~15 seconds
- **Output Size**: 1.5 MB markdown file
- **Lines Processed**: 28,816 lines
- **Output**: Clean, structured Markdown with preserved hierarchy

## License

This project is provided as-is for educational and practical use.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Tips

1. **Large PDFs**: The tool handles large documents efficiently with progress indicators
2. **Encoding**: Uses UTF-8 encoding for proper French character support
3. **Structure**: Automatically detects hierarchical legal document structure
4. **Clean Output**: Removes page numbers and headers automatically

## Troubleshooting

### Issue: Module not found

Make sure dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: Permission denied

Ensure the PDF file is readable and the output directory is writable.

### Issue: Encoding errors

The tool uses UTF-8 encoding by default. If you encounter encoding issues, ensure your PDF contains valid text (not scanned images).

## Future Enhancements

- Support for scanned PDFs (OCR integration)
- Configurable formatting rules via JSON/YAML
- Support for other legal document formats
- Table extraction and formatting
- Export to other formats (HTML, DOCX)

## Workflow Summary

This application reproduces the exact workflow used to convert the Quebec Civil Code PDF to Markdown:

1. **Extract** raw text from PDF using PyMuPDF
2. **Parse** document structure (hierarchical headings, sections, articles)
3. **Format** into clean Markdown with appropriate heading levels
4. **Output** a well-structured `.md` file

The result is a readable, navigable Markdown document that preserves the original structure and content of the legal document.
