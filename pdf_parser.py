"""
Extract data from PDFs
@author Oleksandr Kudriavchenko

Copyright 2024 Johannes Kepler University Linz
LIT Cyber-Physical Systems Lab
All rights reserved
"""
from pypdf import PdfReader 


def get_thesis_data(file_path):
    """
    Gets a path to a pdf file
    Returns all text from file    
    """
    result_text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        result_text += str(page.extract_text())

    return result_text

if __name__=="__main__":
    print(get_thesis_data("1.pdf"))

