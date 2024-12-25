"""
Main file that unites all other parts
@author Oleksandr Kudriavchenko

Copyright 2024 Johannes Kepler University Linz
LIT Cyber-Physical Systems Lab
All rights reserved
"""

from pdf_parser import *
from keywords import *
from database_manager import *
from glob import glob
from time import sleep
from matching import rating


user_interests ={}
already_asked_questions=[]

def generate_db():
    """
    Adds topics from PDF's
    to database
    """
    for file in glob("./Theses_Docs/*.pdf"):
        insert_db(get_keywords(get_thesis_data(file)))
        sleep(30)

    generate_vectors()


def generate_questions(number):
    while 1:
        keyword = get_n_random_keywords(number)[0]
        keyword=keyword.replace("\n","").replace("  "," ")
        if not keyword in already_asked_questions:
            already_asked_questions.append(keyword)
            break 


    questions={}
    
    questions_template=[

        f"How proficient are you with {keyword} (0-10)?",
        f"How often do you use {keyword} in your daily work (0-10)?",
        f"How familiar are you with the concepts of {keyword} (0-10)?",
        f"How experienced are you with {keyword} (0-10)?",
        f"How interested are you in {keyword} (0-10)?"


        ]

    questions[keyword]=questions_template[randint(0,len(questions_template)-1)]

    """questions_template=[
        f"How often do you use {keyword} in your daily work (0-10)?",
        f"How satisfied are you with your current {keyword} (0-10)?",
        f"How important is a good {keyword} to your productivity (0-10)?",
        f"How comfortable are you with {keyword} (0-10)?",
        f"How skilled are you at using {keyword} (0-10)?",
        f"How much do you like {keyword}?",
        f"How important is {keyword} to you?",
        f"How often do you think about {keyword}?",
        f"How satisfied are you with your current {keyword}?"]"""

    return questions




for i in get_all_keywords():
        user_interests[i]=5 #user is neutral in the begining

def assign_values(key, answer):
    
    global user_interests
    if key in get_all_keywords():
        user_interests[key]=answer
                
                

def generate_new_list():
    """
    Returns a sorted list of filtered topics 
    """
    distance_dict=(rating(user_interests,get_name_vector()))

    sorted_list=[k if v>0 else 0 for k, v in sorted(distance_dict.items(),key=lambda item: item[1])]
    
    clean_list=[]
    for i in sorted_list:
        if i:
            clean_list.append(i)
    return clean_list

def show_history(user_interests,already_asked):
    history={}
    
    for key,value in (user_interests.items()):
        if key in already_asked[:-1]:
            history[key]=value
        """
        else:
            print(already_asked)
            print(already_asked_questions)
            """

    return history