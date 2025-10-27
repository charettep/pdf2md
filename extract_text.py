#!/usr/bin/env python3
"""
Extract raw text from PDF using PyMuPDF (fitz) and PyPDF2
"""

import pymupdf  # PyMuPDF
import PyPDF2
import sys

def extract_with_pymupdf(pdf_path):
    """Extract text using PyMuPDF (generally better quality)"""
    print("Extracting with PyMuPDF...")
    text = []

    doc = pymupdf.open(pdf_path)
    for page_num, page in enumerate(doc, 1):
        page_text = page.get_text()
        text.append(f"\n{'='*80}\n")
        text.append(f"PAGE {page_num}\n")
        text.append(f"{'='*80}\n\n")
        text.append(page_text)

    doc.close()
    return ''.join(text)

def extract_with_pypdf2(pdf_path):
    """Extract text using PyPDF2 (alternative method)"""
    print("Extracting with PyPDF2...")
    text = []

    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            text.append(f"\n{'='*80}\n")
            text.append(f"PAGE {page_num + 1}\n")
            text.append(f"{'='*80}\n\n")
            text.append(page_text)

    return ''.join(text)

if __name__ == "__main__":
    pdf_file = "ccq-1991.pdf"

    # Extract with PyMuPDF
    pymupdf_text = extract_with_pymupdf(pdf_file)
    with open("ccq-1991_pymupdf.txt", "w", encoding="utf-8") as f:
        f.write(pymupdf_text)
    print(f"✓ PyMuPDF extraction saved to: ccq-1991_pymupdf.txt")
    print(f"  Length: {len(pymupdf_text)} characters")

    # Extract with PyPDF2
    pypdf2_text = extract_with_pypdf2(pdf_file)
    with open("ccq-1991_pypdf2.txt", "w", encoding="utf-8") as f:
        f.write(pypdf2_text)
    print(f"✓ PyPDF2 extraction saved to: ccq-1991_pypdf2.txt")
    print(f"  Length: {len(pypdf2_text)} characters")

    print("\nDone! Text extraction complete.")
