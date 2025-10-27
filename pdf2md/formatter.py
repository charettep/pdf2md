"""
Markdown formatting module for legal documents
"""

import re


class MarkdownFormatter:
    """Format extracted text into structured Markdown"""

    def __init__(self, raw_text, document_title="Legal Document"):
        """
        Initialize the formatter

        Args:
            raw_text (str): Raw extracted text from PDF
            document_title (str): Title for the document
        """
        self.raw_text = raw_text
        self.document_title = document_title

    def format_to_markdown(self):
        """
        Convert raw text to structured markdown

        Returns:
            str: Formatted markdown text
        """
        # Split by page markers and rejoin content
        pages = re.split(r'={80,}\nPAGE \d+\n={80,}\n', self.raw_text)

        # Start with document header
        markdown_lines = []
        markdown_lines.append(f"# {self.document_title}\n")
        markdown_lines.append("*À jour au 30 juin 2025*\n")
        markdown_lines.append("*© Éditeur officiel du Québec*\n\n")
        markdown_lines.append("---\n\n")

        # Process content (skip first empty split)
        full_text = '\n\n'.join(pages[1:]) if len(pages) > 1 else pages[0]

        lines = full_text.split('\n')
        total_lines = len(lines)

        for i, line in enumerate(lines):
            line = line.strip()

            # Progress indicator
            if i % 1000 == 0 and i > 0:
                print(f"  Processing line {i}/{total_lines}...", end='\r')

            if not line:
                markdown_lines.append('\n')
                continue

            # Skip page footers/headers
            if self._is_page_metadata(line):
                continue

            # Process different structural elements
            formatted = self._format_line(line)
            markdown_lines.append(formatted)

        print(f"\n  ✓ Processed {total_lines} lines")

        return ''.join(markdown_lines)

    def _is_page_metadata(self, line):
        """Check if line is page metadata to skip"""
        metadata_patterns = [
            'À jour au', '© Éditeur officiel', 'CCQ-1991 /', 'CODE CIVIL'
        ]
        return any(pattern in line for pattern in metadata_patterns)

    def _format_line(self, line):
        """
        Apply markdown formatting rules to a line

        Args:
            line (str): Line to format

        Returns:
            str: Formatted line with markdown syntax
        """
        # DISPOSITION PRÉLIMINAIRE
        if 'DISPOSITION PRÉLIMINAIRE' in line or 'DISPOSITION PRELIMINAIRE' in line:
            return f"## {line}\n\n"

        # TABLE DES MATIÈRES
        if 'TABLE DES MATIÈRES' in line or 'TABLE DES MATIERES' in line:
            return f"## {line}\n\n"

        # LIVRE (BOOK level - highest)
        if line.startswith('LIVRE '):
            return f"## {line}\n\n"

        # TITRE (TITLE level)
        if line.startswith('TITRE '):
            return f"### {line}\n\n"

        # CHAPITRE (CHAPTER level)
        if line.startswith('CHAPITRE '):
            return f"#### {line}\n\n"

        # SECTION level
        if line.startswith('SECTION '):
            return f"##### {line}\n\n"

        # § (paragraph/subsection markers)
        if line.startswith('§'):
            return f"###### {line}\n\n"

        # Detect all-caps headers (other structural elements)
        if line.isupper() and len(line) > 10 and not line.startswith('DE '):
            return f"**{line}**\n\n"

        # "DE/DES/DU" titles that are structural
        if re.match(r'^(D[EU]S?|DU)\s+[A-ZÀÂÄÇÈÉÊËÎÏÔÙÛÜ]', line) and line.isupper():
            # Check if it looks like a heading (relatively short, all caps)
            if len(line) < 100 and '...' not in line:
                return f"**{line}**\n\n"

        # Dotted lines with page numbers (table of contents entries)
        if '...' in line and re.search(r'\d+$', line):
            parts = line.split('...')
            if len(parts) == 2:
                title = parts[0].strip()
                page_num = parts[1].strip()
                return f"- {title} `{page_num}`\n"

        # Regular article numbers (like "50", "55", etc. at start of line)
        if re.match(r'^\d+[\.\,]?\s*$', line):
            return f"`Article {line.strip('.,')}`\n\n"

        # Lines that end with article references (e.g., "1991, c. 64, préam.")
        if re.search(r'\d{4},\s*c\.\s*\d+', line):
            return f"*{line}*\n\n"

        # Chapter/section notation with Roman numerals (I. —, II. —, etc.)
        if re.match(r'^[IVX]+\.\s*—', line):
            return f"**{line}**\n\n"

        # Regular content
        return f"{line}\n"

    def save_markdown(self, output_path):
        """
        Format and save markdown to file

        Args:
            output_path (str): Path to save the markdown file

        Returns:
            str: The formatted markdown text
        """
        markdown = self.format_to_markdown()

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"  ✓ Markdown saved to: {output_path}")
        print(f"  Length: {len(markdown)} characters")

        return markdown
