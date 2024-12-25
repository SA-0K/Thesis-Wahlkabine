"""
Mathcing user choices to topics. Generating rating
@author Oleksandr Kudriavchenko

Copyright 2024 Johannes Kepler University Linz
LIT Cyber-Physical Systems Lab
All rights reserved
"""


from math import sqrt


def Euclidean_matching(User,Topic):
    """
    Takes topic and user interests vectors
    returns distance between them
    
    Filters topic if user interest is in [0;3)
    """
    result=0
    for interest,user_value in User.items():
        try: # In case of mismatching with databse
            user_value -= 3   # move scale from [0;10] to [-3;7]
            topic_keyword_value = Topic[interest]
            result += (user_value-topic_keyword_value)**2
            #print(user_value,topic_keyword_value)
            if user_value*topic_keyword_value<0:
                return -1 # Topic is filtered (not interested for the user)
            
        except:pass
    return sqrt(result)
    

def rating(user_interests:dict,topics_with_names:list):
    """
    Returns a dictionary with topics distances to user's interests 
    """
    topic_distance_list={}
    for Topic in topics_with_names: 
        topic_distance_list[Topic["name"]]=Euclidean_matching(user_interests,Topic["vector"])

    return topic_distance_list


