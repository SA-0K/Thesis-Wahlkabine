# Thesis-Walkhabine

This project is created to help students in choosing a topic for a thesis based on their interests and knowledge. 

## Information

### User's session data
All information about student's choises is stored in a dictionary called `main.user_interests`.
The keys are keywords from existing topics and the values are represented with floating point number from 0 to 10.

A list `main.already_asked_questions` stores keywords that have already been used for generating a questions. This is done to avoid repeating questions.

### Question generation
The questions are generated from templates like these:
```
f"How experienced are you with {keyword} (0-10)?"
f"How skilled are you at using {keyword} (0-10)?"
f"How interested are you in {keyword} (0-10)?"
```
It it is done by function `main.generate_questions()`.
It extracts n random keywords from database (`database_manager.get_n_random_keywords()`) and returns a dictionary where key is a keyword and value is a random questions from tamplate list.

### Keyword extraction
It is done by using natural language processing. The funcrion gets raw text from file and returns that data :
```
return name, supervisor, descryption, keywords
```


### Matching
The matching is done by using an Euclidean distance formula. User choices are represented as a point in multidirectional coordinate system as well as the topics. 



## Usage

Firstly call `databse_manager.generate_databbase()` to create a database from theses descryption files.
They should be stored in Theses_Docs directory and have a pdf extension.

Call the `main.init()` function to fill `main.user_interests` dictionary with neutral values (range of values is from 0 to 10, so neutral one is 5) .