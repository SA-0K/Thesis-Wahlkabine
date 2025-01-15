"""
Extracting data from plaintext
@author Oleksandr Kudriavchenko

Copyright 2024 Johannes Kepler University Linz
LIT Cyber-Physical Systems Lab
All rights reserved
"""

import google.generativeai as genai
from key import *
genai.configure(api_key=KEY)
model = genai.GenerativeModel("gemini-1.5-flash")




data_example="""Current Situation
Extracting variability information from source code or other artifact types
of a set of given product variants is a complex task that requires differ-
encing files. This is currently mostly done by performing simple line-by-
line comparisons. Even though these approaches are sufficient for de-
tecting major additions or deletions, they are not well-suited for identify-
ing and extracting variability. While there exist tools that better support
these tasks, they are mostly restricted to specific use-cases.
Background
Software Product Lines (SPL) allow systematic reuse of common code across different variants of a
system. While this approach is well-known, due to high upfront effort this technique is often not applied
from project startup. When the number and size of variants increase over time, at some point it is no
longer possible to maintain and manage variability. At this point, the transformation into a SPL is de-
sired. However, doing this manually is not feasible. Therefore, automatically extracting and analyzing
variability information is needed. An approach, that can perform this process for any type and combi-
nation of artifact types is currently in development, which utilizes extractors for individual artifacts.
Content of the Thesis
The goal of this thesis is to develop an extractor, that can compare an arbitrary number of variant files
of a specific artifact type (e.g., source code of a programming language, spreadsheets, config files
etc.) for commonalities/variabilities, filter them for relevance (e.g., moved code, split statements can be
omitted) and provides information about their occurrences (in which variant does variability x appear).
The artifact type, for which the extractor is written, can be chosen based on the interest and
knowledge of the student. Integrating this extractor into a flexible framework for variability mining is
also desired. The extraction process itself should be implemented and tested using Java."""


def get_keywords(thesis_text):
    keywords = str(model.generate_content(f"You're creating a data for database. Generate, please, keywords that are really related to thesis based on this descryption:{thesis_text}. Do not add additional explanations, just plaintext keyword array delimited with semicolons that will be processed by another app").text).split(';')
    
    name = str(model.generate_content(f"You're creating a data for database. Extract, please, name of the thesis topic descryption:{thesis_text}. Do not add any additional information or text, just a name as it's written in the file").text)
    descryption= str(model.generate_content(f"You're creating a data for database. Extract, please, descryption of the thesis topic:{thesis_text}. Do not add any additional information, give a short descryption,please").text)
    supervisor = str(model.generate_content(f"You're creating a data for database. Extract, please, supervisors names:{thesis_text}. Do not add any additional information, please").text)
    
    return name, supervisor, descryption, keywords



if __name__=="__main__":
    print(get_keywords(data_example))