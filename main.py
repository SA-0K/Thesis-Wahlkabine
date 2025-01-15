"""
Main file that unites all other parts
@author Oleksandr Kudriavchenko

Copyright 2024 Johannes Kepler University Linz
LIT Cyber-Physical Systems Lab
All rights reserved
"""
import database_manager
from random import randint
from matching import rating


user_interests = {}        # stores user's choices 
already_asked_questions=[] # stores asked questions, so they do not repeat



def generate_questions(number):

    """
    Generates specified number of questions.
    Returns a dictionary
    """
    questions={}
    while number>0:
        keyword = database_manager.get_n_random_keywords(1)[0]
        keyword=keyword.replace("\n","").replace("  "," ")

        if not keyword in already_asked_questions:
            already_asked_questions.append(keyword)
            number-=1
        
             


            
            questions_template=[

                f"How proficient are you with {keyword} (0-10)?",
                f"How often do you use {keyword} in your daily work (0-10)?",
                f"How familiar are you with the concepts of {keyword} (0-10)?",
                f"How experienced are you with {keyword} (0-10)?",
                f"How skilled are you at using {keyword} (0-10)?",
                f"How interested are you in {keyword} (0-10)?"


                ]


            # adding a random question and its keyword to dictionary of questions
            questions[keyword]=questions_template[randint(0,len(questions_template)-1)]

    return questions




def assign_values(key, answer):
    """
    Updates user_interests dictionary
    """
    global user_interests
    if key in database_manager.get_all_keywords():
        user_interests[key]=answer
                
                

def generate_new_topic_list():
    """
    Returns a sorted list of filtered topics 
    """
    distance_dict=(rating(user_interests,database_manager.get_name_vector()))

    sorted_list=[k if v>0 else 0 for k, v in sorted(distance_dict.items(),key=lambda item: item[1])]
    
    clean_list=[]
    for data in sorted_list:
        # if element is not ''
        if data: 
            clean_list.append(data)
    return clean_list

def generate_history():
    """
    Returns a history dictionary based on user interests and asked questions
    """
    history={}
    
    for key,value in (user_interests.items()):
        # Do not use the last one in array. 
        # It is still in the main window, so it won't be in history yet.
        if key in already_asked_questions[:-1]:
            history[key]=value

    return history

def init():
    for key in database_manager.get_all_keywords():
            user_interests[key] = 5 # user is neutral in the begining
