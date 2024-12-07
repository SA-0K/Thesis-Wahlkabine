from math import sqrt


def Euclidean(x,y):
    if len(x)==len(y):
        result=0
        for i,a in enumerate(x):
            b=y[i]
            result+= (a-b)**2
        return sqrt(result)
    else:
        return 100 # Error code, returning distance that is bigger than diagnal


def Euclidean_matching(User,Topic):
    
    result=0
    for interest,value in User.items():
        try: # Maybe mismatching vith databse
            topic_keyword_value=Topic[interest]
            result+= (value-topic_keyword_value)**2
        except:pass
    return sqrt(result)
    

def rating(user,topics_with_names):
    topic_distance_list={}
    for Topic in topics_with_names: 
        topic_distance_list[Topic["name"]]=Euclidean_matching(user,Topic["vector"])

    return topic_distance_list


"""
---------Experiment---------
----Comparing algorythms----


Input data:
a=[0,10,8,5]
b=[10,10,10,10]
c=[0,10,10,10]
d=[0,10,0,0]

Euclidean (Works good)
b  11.357816691600547       4th place (topic has something than not interesting for student)
c  5.385164807134504        2nd place (no excessive keywords/interests)
d  9.433981132056603        3rd place (topic has something interesting for student and nothing that is not interesting to him, 
                                       but there are better choices)
a  0.0                      1st place (Best matching of topic and student's interests)

Inner product (Works bad)
(good and worst options give us the same result)
b  230
c  230
d  100
a  189


Cheking if not zero (Works bad)
(best, good and worst options give us the same result)
b  3
c  3
d  1
a  3

"""


def testing(VECT_DIMENTION,RUNS):
    from numpy import dot as inner_product
    from random import randint
    import time
    
    t1=[]
    t2=[]
    for i in range(RUNS):
        a=[]
        b=[]
        for i in range(VECT_DIMENTION):
            a.append(randint(0,10))
            b.append(randint(0,1)*10)

        start = time.time()
        inner_product(a,b)
        t1.append(time.time()-start)


        start = time.time()
        Euclidean(a,b)
        t2.append(time.time()-start)

    print(f"Inner product: {sum(t1)/len(t1)}\nEuclidean distance: {sum(t2)/len(t2)}\n")


    """

    ----Execution time for 20 000+ Keywords----
    ----------(Avarage for 100 runs)-----------

    Inner product:      0.010788238048553467
    Euclidean distance: 0.011116526126861571

    
    """

