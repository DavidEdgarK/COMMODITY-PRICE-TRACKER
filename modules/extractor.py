"""
This module will locate and extract tables from pdfs
"""
from pathlib import Path
import pdfplumber
import camelot
import pandas as pd

file_path = "C:\Users\admin\Desktop\CODING PROJECTS & PRACTICES\PYTHON PROJECTS\COMMODITY-PRICE-TRACKER\reports"

def open_pdf(file_path):
    """Load the pdf files"""
    with open(file_path) as pdf_files:
        content = pdf_files.read()
    return content

def extract_text(page):
    """Pull text for keyword scanning"""

def extract_tables_camelot(file_path, pages):
    """Structured table extraction with camelot"""

def extract_tables_plumber(pages):
    """A fallback table extraction with pdfplumber"""

def ocr_fallback(image_page):
    """OCR for scanned pages"""

def merge_tables(tables_list):
    """unify the outputs from multiple tools""""""
This module will locate and extract tables from pdfs
"""
from pathlib import Path
import pdfplumber
import camelot
import pandas as pd

file_path = "C:\Users\admin\Desktop\CODING PROJECTS & PRACTICES\PYTHON PROJECTS\COMMODITY-PRICE-TRACKER\reports"

def open_pdf(file_path):
    """Load the pdf files"""
    with open(file_path) as pdf_files:
        content = pdf_files.read()
    return content

def extract_text(page):
    """Pull text for keyword scanning"""

def extract_tables_camelot(file_path, pages):
    """Structured table extraction with camelot"""

def extract_tables_plumber(pages):
    """A fallback table extraction with pdfplumber"""

def ocr_fallback(image_page):
    """OCR for scanned pages"""

def merge_tables(tables_list):
    """unify the outputs from multiple tools"""