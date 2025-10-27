"""
Setup configuration for PDF to Markdown converter
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name='pdf2md-legal',
    version='1.0.0',
    description='Convert PDF legal documents to structured Markdown format',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='PDF2MD Project',
    python_requires='>=3.7',
    packages=find_packages(),
    install_requires=[
        'PyMuPDF>=1.23.0',
        'PyPDF2>=3.0.0',
    ],
    entry_points={
        'console_scripts': [
            'pdf2md=pdf2md.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Legal Industry',
        'Topic :: Text Processing :: Markup :: Markdown',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='pdf markdown converter legal documents',
)
