from pdf_parser import *
from keywords import *
from database_manager import *
from glob import glob
from time import sleep
from matching import rating


def generate_db():
    for file in glob("./Theses_Docs/*.pdf"):
        insert_db(get_keywords(get_thesis_data(file)))
        sleep(30)

    generate_vectors()

"""
for i in range(1,4):
    try:
        insert_db(get_keywords(get_thesis_data(f"{i}.pdf")))
    except:
        print(f"{i}. :o ")
"""
#generate_db()
#print_db()
already_been_asked=[]
def generate_questions(number):
    while 1:
        keyword = get_questions_keywords(number)[0]
        keyword=keyword.replace("\n","").replace("  "," ")
        if not keyword in already_been_asked:
            already_been_asked.append(keyword)
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


print_db()

user_interests ={}


def temp_sol(tmp,answer):
    return 
    """tmp=generate_questions(1)
    for key, val in tmp.items():
        print(val)
        curr_q=val
        #answer=int(input())
        tmp[key]=answer"""
for i in get_all_keywords():
        user_interests[i]=0
def assign_values(key, answer):
    
    global user_interests
    if key in get_all_keywords():
        user_interests[key]=answer
                #print(answer)

    #print(user_interests)

def generate_new_dict():
    distance_dict=(rating(user_interests,get_name_vector()))


    sorted_dict={k: v for k, v in sorted(distance_dict.items(),key=lambda item: item[1])}
    return (sorted_dict)

def show_history(user_interests,already_asked):
    history={}
    
    for key,value in sorted(user_interests.items()):
        if key in already_asked[:-1]:
            history[key]=value
        else:
            print(already_asked)
            print(already_been_asked)

    return history