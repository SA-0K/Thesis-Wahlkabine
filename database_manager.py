"""
Creating, editing and reading database
@author Oleksandr Kudriavchenko

Copyright 2024 Johannes Kepler University Linz
LIT Cyber-Physical Systems Lab
All rights reserved
"""

import pymongo
from random import randint

from keywords import get_keywords
from pdf_parser import get_thesis_data

from glob import glob
from time import sleep

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
database = myclient["Database_"]
records = database["Theses"]

def insert_database(data_array):
    """
    Adds a new topic to database
    """
    name, supervisor, descryption, keywords = data_array[0], data_array[1], data_array[2], data_array[3] 
    database_dictionary = { "name":name, "supervisor":supervisor, "descryption":descryption, "keywords":keywords }
    records.insert_one(database_dictionary)
    
    

def print_database():
    """
    Prints all database fields into a terminal
    """
    for record in records.find():
        print(record)


def get_name_vector():
    """
    Returns an array of dictionaries
    [{name:"a",vector:"1 1 1"},
     {name:"b",vector:"2 3 7"}]
    """
    result =[]
    for record in records.find():
        name_vector_dictionary = {}
        name_vector_dictionary["name"]=record["name"]
        name_vector_dictionary["vector"]=record["vector"]
        result.append(name_vector_dictionary)
    return result

def get_all_keywords():
    """
    Returns an array of all keywords from all topics
    """
    all_keywords=[]
    for record in records.find():
        for key in record["keywords"]:
            if not key in all_keywords:
                all_keywords.append(key)#.replace("\n","").replace("  "," "))
    return all_keywords

def generate_vectors():
    """
    Generates positions for topics on a coordinate axis
    """

    all_keywords=get_all_keywords()

    for record in records.find():
        vector = {}
        for key in all_keywords:
            # if keyword is in the topic give it value 10, else 0
            if key in record["keywords"]:
                vector[f"{key}"]=10
            else:
                vector[f"{key}"]=0

        # adding/updating a vector to each record
        records.update_one({"_id":record["_id"]},{"$set":{"vector":vector}})   
    
    
def change_requirment(topic,picked_keyword,new_value):

    """
    Function for adding crucial requirements to a student
    """

    for record in records.find():

        if record['name']==topic:
        
            for key in record["keywords"]:
        
                if key==picked_keyword:

                    # extract vector
                    vector = record["vector"]
                    # edit value           
                    vector[picked_keyword] = new_value  
                    # write vector back
                    records.update_one({"_id":record["_id"]},{"$set":{"vector":vector}})   

                    return
    

def generate_database():
    """
    Adds topics from PDF's
    to database
    """
    for file in glob("./Theses_Docs/*.pdf"):
        try:
            insert_database(get_keywords(get_thesis_data(file)))
            print(file)
        except Exception as e:
            print(e)
        sleep(30)

    generate_vectors()

def get_n_random_keywords(n):
    """
    Returns an array of n random keywords
    
    """
    result = []
    all_keywords=get_all_keywords()
    
    while n>0:

        keyword = all_keywords[randint(0, len(all_keywords)-1)]

        # do not add copies
        if not keyword in result:
            result.append(keyword)
            n-=1

    return result


if __name__=="__main__":
    print_database()
    