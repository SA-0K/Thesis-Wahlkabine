# Thesis-Wahlkabine

This project is created to help students in choosing a topic for a thesis based on their interests and knowledge. 

![](https://github.com/SA-0K/Thesis-Wahlkabine/blob/main/thesiswahlkabine.GIF)

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
### Important information about `keywords.py`
There is an example file that uses Gemini API. The model called Gemini 1.5 Flash.
Information from ai.google.dev:

"The Gemini API “free tier” is offered through the API service with lower rate limits for testing purposes. Google AI Studio usage is completely free in all [available countries](https://ai.google.dev/gemini-api/docs/available-regions)."

### Matching
The matching is done by using an Euclidean distance formula. User choices are represented as a point in multidirectional coordinate system as well as the topics. 

The function for it called `matching.Euclidean_matching(User,Topic)`.
For each keyword we do this calculation:
```
result += (user_value-topic_keyword_value)**2
```
And returning the square root of `result` in the end.
But there also is a `filter` variable. If user choice is less than `filter`, then the topic is not interesting for him and will be hidden (return negative distance).
If the value for a keyword is more than 10, it means that there is a supervisor's requirement. If user do not satisfy the it, then the topic also will be hidden (return negative distance).

### Requirements
It is done by `change_requirment(topic,picked_keyword,new_value)` function. 
By default all keywords that are present in the topic hae value 10, but if supervisor wants to create a requirement, he/she should set the value in range from 10 to 20.

For example the value is 17.
10 indicates, that keyword is present in this topic.
7 is the requirement (gate value). If user answers the question with his value less than 7, the topic will be hidden from him.

## Usage

Firstly call `databse_manager.generate_databbase()` to create a database from theses descryption files.
They should be stored in Theses_Docs directory and have a pdf extension.

0. Call the `main.init()` function to fill `main.user_interests` dictionary with neutral values (range of values is from 0 to 10, so neutral one is 5) .

1. Use the function `main.generate_questions(number)` to generate questions for the user.
2. Then ask him for an input on a scale from 0 to 10.
3. Use the function `main.assign_values()` to update `main.user_interests` dictionary.
4. Call `main.generate_new_topic_list()` to update the values of topic distances. It will return a sorted list of topics, where first elements are the most recomended to a user.
5. Repeat from step (1)



You can find how all functionality used in `gui.py` and `requirments_gui.py` as they are crated for feature demonstrations.
