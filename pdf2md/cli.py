"""
Command-line interface for PDF to Markdown converter
"""

import argparse
import os
import sys
from pathlib import Path

from .extractor import PDFExtractor
from .formatter import MarkdownFormatter


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Convert PDF legal documents to structured Markdown format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s document.pdf                    # Creates document.md
  %(prog)s document.pdf -o output.md       # Specify output file
  %(prog)s document.pdf --title "My Doc"   # Custom document title
  %(prog)s document.pdf --save-raw         # Also save raw text extraction
        """
    )

    parser.add_argument(
        'input_pdf',
        help='Path to input PDF file'
    )

    parser.add_argument(
        '-o', '--output',
        help='Output markdown file path (default: input filename with .md extension)',
        dest='output_md'
    )

    parser.add_argument(
        '-t', '--title',
        help='Document title for the markdown file (default: extracted from filename)',
        dest='title'
    )

    parser.add_argument(
        '--save-raw',
        action='store_true',
        help='Save raw extracted text to .txt file',
        dest='save_raw'
    )

    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s 1.0.0'
    )

    args = parser.parse_args()

    # Validate input file
    if not os.path.isfile(args.input_pdf):
        print(f"Error: Input file '{args.input_pdf}' not found", file=sys.stderr)
        sys.exit(1)

    if not args.input_pdf.lower().endswith('.pdf'):
        print(f"Warning: Input file '{args.input_pdf}' does not have .pdf extension")

    # Determine output paths
    input_path = Path(args.input_pdf)
    base_name = input_path.stem

    if args.output_md:
        output_md = args.output_md
    else:
        output_md = str(input_path.with_suffix('.md'))

    output_raw = str(input_path.with_suffix('.txt'))

    # Determine document title
    if args.title:
        doc_title = args.title
    else:
        # Generate title from filename
        doc_title = base_name.upper().replace('-', ' ').replace('_', ' ')

    # Print banner
    print("=" * 80)
    print("PDF to Markdown Converter for Legal Documents")
    print("=" * 80)
    print(f"\nInput PDF:     {args.input_pdf}")
    print(f"Output MD:     {output_md}")
    if args.save_raw:
        print(f"Raw text:      {output_raw}")
    print(f"Document title: {doc_title}")
    print()

    try:
        # Step 1: Extract text from PDF
        print("[1/3] Extracting text from PDF...")
        extractor = PDFExtractor(args.input_pdf)
        raw_text = extractor.extract_text()

        # Optionally save raw text
        if args.save_raw:
            with open(output_raw, 'w', encoding='utf-8') as f:
                f.write(raw_text)
            print(f"  ✓ Raw text saved to: {output_raw}")

        # Step 2: Format to markdown
        print("\n[2/3] Formatting to Markdown...")
        formatter = MarkdownFormatter(raw_text, document_title=doc_title)
        markdown = formatter.format_to_markdown()

        # Step 3: Save markdown
        print("\n[3/3] Saving Markdown file...")
        with open(output_md, 'w', encoding='utf-8') as f:
            f.write(markdown)
        print(f"  ✓ Markdown saved to: {output_md}")

        # Success summary
        print("\n" + "=" * 80)
        print("✓ Conversion completed successfully!")
        print("=" * 80)
        print(f"\nOutput file: {output_md}")
        print(f"File size:   {len(markdown):,} characters")
        print()

    except Exception as e:
        print(f"\n✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
