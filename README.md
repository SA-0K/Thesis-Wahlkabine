# Thesis-Walkhabine

This project is created to help students in choosing a topic for a thesis based on their interests and knowledge. 

## Information

### User's session data
All information about student's choises is stored in a dictionary called `user_interests`.
The keys are keywords from existing topics and the values are represented with floating point number from 0 to 10.

A list `already_asked_questions` stores keywords that have already been used for generating a questions. This is done to avoid repeating questions.

### Question generation
The questions are generated from templates like these:
```
f"How experienced are you with {keyword} (0-10)?"
f"How skilled are you at using {keyword} (0-10)?"
f"How interested are you in {keyword} (0-10)?"
```

### Keyword extraction
It is done by using natural language processing. The funcrion gets raw text from file and returns that data :
```
return name, supervisor, descryption, keywords
```


### Matching
The matching is done by using an Euclidean distance formula. User choices are represented as a point in multidirectional coordinate system as well as the topics. 

## Usage

Firstly call `generate_db()` to create a database from theses descryption files.
They should be stored in Theses_Docs directory and have a pdf extension.

```
for i in get_all_keywords():
       user_interests[i] = 5
```
This part is used to make user's interests neutral when he opens the application.
User can evaluate his interests on scale from 0 to 10, so 5 is neutral value.
