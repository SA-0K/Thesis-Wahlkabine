"""
Creating, editing and reading database
@author Oleksandr Kudriavchenko

Copyright 2024 Johannes Kepler University Linz
LIT Cyber-Physical Systems Lab
All rights reserved
"""

import pymongo
from random import randint


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["Database_"]
col = db["Theses"]

def insert_db(arr):
    """
    Adds a new topic to database
    """
    name, supervisor, descryption, keywords = arr[0], arr[1], arr[2], arr[3] 
    mydict = { "name":name, "supervisor":supervisor, "descryption":descryption, "keywords":keywords }
    col.insert_one(mydict)
    
    

def print_db():
    for c in col.find():
        print(c)


def get_name_vector():
    """
    Returns an array of dictionaries
    [{name:"a",vector:"1 1 1"},
     {name:"b",vector:"2 3 7"}]
    """
    result =[]
    for c in col.find():
        tmp = {}
        tmp["name"]=c["name"]
        tmp["vector"]=c["vector"]
        result.append(tmp)
    return result

def get_all_keywords():
    all_keywords=[]
    for c in col.find():
        for k in c["keywords"]:
            if not k in all_keywords:
                all_keywords.append(k)#.replace("\n","").replace("  "," "))
    return all_keywords

def generate_vectors():
    """
    Generates positions for topics on a coordinate axis
    """

    all_keywords=get_all_keywords()

    for c in col.find():
        vect={}
        for k in all_keywords:
            if k in c["keywords"]:
                vect[f"{k}"]=10
            else:
                vect[f"{k}"]=0
        col.update_one({"_id":c["_id"]},{"$set":{"vector":vect}})   
    
    
def change_requirment(topic,keyword,value):
    for c in col.find():
        if c['name']==topic:
            for i in c["keywords"]:
                if i==keyword:
                    vector = c["vector"]
                    vector[keyword]=value
                    col.update_one({"_id":c["_id"]},{"$set":{"vector":vector}})   

                    return
    


def get_n_random_keywords(n):
    result = []
    tmp=[]

    for c in col.find():
        tmp+=(c["keywords"])
    
    while n>0:
        keyword=tmp[randint(0, len(tmp)-1)]
        if not keyword in result:
            result.append(keyword)
            n-=1
    return result

def delete_db():
    
    db.col.delete_many({"name":"DEVELOPING AN EXTRACTOR FOR MINING VARIABILITY FROM PRODUCT VARIANTS\n"})
    #col = db["Theses"]


if __name__=="__main__":
    #print(get_name_vector())
    generate_vectors()
    print_db()
    