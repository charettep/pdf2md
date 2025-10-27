"""
PDF text extraction module using PyMuPDF
"""

import pymupdf  # PyMuPDF


class PDFExtractor:
    """Extract raw text from PDF files using PyMuPDF"""

    def __init__(self, pdf_path):
        """
        Initialize the PDF extractor

        Args:
            pdf_path (str): Path to the PDF file
        """
        self.pdf_path = pdf_path
        self.doc = None

    def extract_text(self):
        """
        Extract text from PDF with page markers

        Returns:
            str: Extracted text with page separators
        """
        text_parts = []

        try:
            self.doc = pymupdf.open(self.pdf_path)
            total_pages = len(self.doc)

            for page_num, page in enumerate(self.doc, 1):
                # Add page marker
                text_parts.append(f"\n{'='*80}\n")
                text_parts.append(f"PAGE {page_num}\n")
                text_parts.append(f"{'='*80}\n\n")

                # Extract page text
                page_text = page.get_text()
                text_parts.append(page_text)

                # Progress indicator
                if page_num % 10 == 0 or page_num == total_pages:
                    print(f"  Extracted {page_num}/{total_pages} pages...", end='\r')

            print(f"\n  ✓ Extracted {total_pages} pages successfully")

        except Exception as e:
            raise Exception(f"Error extracting text from PDF: {e}")

        finally:
            if self.doc:
                self.doc.close()

        return ''.join(text_parts)

    def save_raw_text(self, output_path):
        """
        Extract and save raw text to file

        Args:
            output_path (str): Path to save the extracted text

        Returns:
            str: The extracted text
        """
        text = self.extract_text()

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)

        print(f"  ✓ Raw text saved to: {output_path}")
        print(f"  Length: {len(text)} characters")

        return text
