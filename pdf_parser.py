"""
Extract data from PDFs
@author Oleksandr Kudriavchenko

Copyright 2024 Johannes Kepler University Linz
LIT Cyber-Physical Systems Lab
All rights reserved
"""
from pypdf import PdfReader 


def get_thesis_data(file):
    result_text =""
    reader = PdfReader(file)
    for page in reader.pages:
        result_text+= str(page.extract_text())

    return result_text

if __name__=="__main__":
    print(get_thesis_data("1.pdf"))

