"""
This module will take the extracted data for cleaning and normalizing the data.
"""
import pandas as pd

def load_raw_excel(file_path):
    """read the raw tables into a DataFrame"""

def standardize_columns(df):
    """rename/normalize column headers"""

def handle_missing_values(df):
    """impute or drop missing entries"""

def convert_data_types(df):
    """ensure numeric columns are standardized either as floats/ints"""
    
def aggregate_indices(df):
    """compute monthly/annual CPI aggregates"""

def save_clean_excel(df,filename):
    """write the cleaned dataset to an excel for downstream use"""