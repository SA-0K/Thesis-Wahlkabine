import pymongo
from random import randint


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["Database_"]
col = db["Theses"]

def insert_db(arr):
    name, supervisor, descryption, keywords = arr[0], arr[1], arr[2], arr[3] 
    mydict = { "name":name, "supervisor":supervisor, "descryption":descryption, "keywords":keywords }
    col.insert_one(mydict)
    
    

def print_db():
    for c in col.find():
        print(c)


def get_name_vector():
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
                all_keywords.append(k.replace("\n","").replace("  "," "))
    return all_keywords

def generate_vectors():

    # CHECK IF 10
    #col.update_many({},{"$set":{"vector":0}} )
    all_keywords=get_all_keywords()

    #print(len(all_keywords))
    for c in col.find():
        vect={}
        for k in all_keywords:
            if k in c["keywords"]:
                vect[f"{k}"]=10
            else:
                vect[f"{k}"]=0
        col.update_one({"_id":c["_id"]},{"$set":{"vector":vect}})   
    
    
        
    





def get_questions_keywords(n):
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
    