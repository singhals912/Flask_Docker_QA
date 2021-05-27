# Assginment2 Documentation

## 1. A listing of available routes/resources along with example requests and responses
There are 2 routes in the Flask App:
  1. /models
     -> 3 methods have been used under this route:
        1. GET: To get the list of all the models. 
           e.g.: https://assgn2tag-isd4ai77qq-oa.a.run.app/models will give the list of all the models as the reponse. 
           #### Response: 
           [
                    {
                        "model": "mrm8488/bert-tiny-5-finetuned-squadv2",
                        "name": "bert-tiny",
                        "tokenizer": "mrm8488/bert-tiny-5-finetuned-squadv2"
                    },
                    {
                        "model": "distilbert-base-uncased-distilled-squad",
                        "name": "distilled-bert",
                        "tokenizer": "distilbert-base-uncased-distilled-squad"
                        
            ]
  3. /answer




## 4. How to build and run the API locally via Docker or Flask
### Steps:
1. To build the API locally, I have used FLASK module in python. After imoporting the dependencines, a name "app" is given using Flask(__ name __). 
2. Now, on the base URL I have created different routes such as models and answer.  Models is to list, delete and add the models and answer is to get the answer on some context and question and list all the answered questions for a particular timestamp range.
3. For each route, I defined all the handlers/functions as per the methods mentioned in the route field. e.g. GET(to request the entire or filtered data), POST (to add new data), PUT(to modify the existing data) and DELETE (to delete data basis some query filter). 
4. Then, I used SQLite3 to create a database and tables. So that data can be inserted into these tables.
5. When everything is setup, I gave it a PORT number on which our flask can be run. 
6. Upon clicking on the given URL, I used this Flask app to get, put, post and delete any row from the database.     
