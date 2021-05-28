# Assginment2 Documentation

## 1. A listing of available routes/resources along with example requests and responses
### There are 2 routes in the Flask App:
#### /models -> 3 methods have been used under this route: 
  #### 1. GET: To get the list of all the models. 
              e.g.: https://assgn2tag-isd4ai77qq-oa.a.run.app//models 
              This will give the list of all the models as the response.
              Response:
              [
                {
                  "model": "distilbert-base-uncased-distilled-squad", 
                  "name": "distilled-bert", 
                  "tokenizer": "distilbert-base-uncased-distilled-squad"
                }, 
                {
                  "model": "deepset/roberta-base-squad2", 
                  "name": "deepset-roberta", 
                  "tokenizer": "deepset/roberta-base-squad2"
                }
              ]


  #### 2. PUT: To add a model in our list of models. 
              e.g.: https://assgn2tag-isd4ai77qq-oa.a.run.app//models 
              This will give the list of all the models in addition to the model we have requested to added in our list of models.

              Request:

              {
              "name": "bert-tiny",
              "tokenizer": "mrm8488/bert-tiny-5-finetuned-squadv2",
              "model": "mrm8488/bert-tiny-5-finetuned-squadv2"
              }

              Response:
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
                }, 
                {
                  "model": "deepset/roberta-base-squad2", 
                  "name": "deepset-roberta", 
                  "tokenizer": "deepset/roberta-base-squad2"
                }
              ]
  #### 3. DELETE: To delete a model in our list of models. 
                e.g.: https://assgn2tag-isd4ai77qq-oa.a.run.app/models?model=bert-tiny
                This will give the list of all the models after the deletion of the model we have requested to be removed in the URL, “bert-tiny” in this case, in our list of models.

                Response:

                [
                  {
                    "model": "distilbert-base-uncased-distilled-squad", 
                    "name": "distilled-bert", 
                    "tokenizer": "distilbert-base-uncased-distilled-squad"
                  }, 
                  {
                    "model": "deepset/roberta-base-squad2", 
                    "name": "deepset-roberta", 
                    "tokenizer": "deepset/roberta-base-squad2"
                  }
                ]

#### /answer -> 2 methods have been used under this route: 
#### 1. ANSWERING A QUESTION
####  POST: To add a question and a context for it in our table, and then get an answer to the question from the context. It also gives the model that is used in order to give us the answer and timestamp in terms of the Unix time.
e.g. https://assgn2tag-isd4ai77qq-oa.a.run.app/answer

        Request:

          {
              "answer": "Leigh-Ann Galloway", 
              "context": "She attended the British drama school East 15 in 2005, and left after winning a high-profile role in the BBC drama Waterloo Road, playing the bully Leigh-Ann Galloway.[6] Since that role, Matthews has continued to act in BBC's Doctors, playing Connie Whitfield; in ITV's The Bill playing drug addict Josie Clarke; and she was back in the BBC soap Doctors in 2009, playing Tansy Flack.", 
              "model": "distilbert-base-uncased-distilled-squad", 
              "question": "who did holly matthews play in waterloo rd?", 
              "timestamp": 1622160458
          }

         Response:

          [
            {
              "answer": "Leigh-Ann Galloway", 
              "context": "She attended the British drama school East 15 in 2005, and left after winning a high-profile role in the BBC drama Waterloo Road, playing the bully Leigh-Ann Galloway.[6] Since that role, Matthews has continued to act in BBC's Doctors, playing Connie Whitfield; in ITV's The Bill playing drug addict Josie Clarke; and she was back in the BBC soap Doctors in 2009, playing Tansy Flack.", 
              "model": "distilbert-base-uncased-distilled-squad", 
              "question": "who did holly matthews play in waterloo rd?", 
              "timestamp": 1622160458
            }
          ]

#### 2. LIST OF RECENTLY ANWERED QUESTIONS
#### GET: We use this when we want to know the questions which were answered with its context between a timeframe (Unix format). We require to give a start and end time in order to get results.
e.g:  https://assgn2tag-isd4ai77qq-oa.a.run.app/answer?start=1622160500.3238049&end=1722001920.9152892

        Response:

        [
          {
            "answer": "Travis Pastrana", 
            "context": "2006 brought footage of Travis Pastrana completing a double backflip on an uphill/sand setup on his popular /Nitro Circus/ Freestyle Motocross movies. On August 4, 2006, at X Games 12 in Los Angeles, he became the first rider to land a double backflip in competition. Having landed another trick that many had considered impossible, he vowed never to do it again.", 
            "model": "distilbert-base-uncased-distilled-squad", 
            "question": "who did the first double backflip on a dirt bike?", 
            "timestamp": 1622161326
          }
        ]

## 2. The general idea behind the API!
_API stands for Application Programming Interface. API allows two different application to communicate with each other. It is the part of the server that receives requests and sends responses. While there are numerous protocols and technologies involved, the underlying purpose of APIs is always the same: to let one piece of software communicate with another._

Usually it’s like a client & server, where the client requests some information from a webserver. The data/info is retrieved mostly in the form of JASON. The client applications aren’t directly linked to the database mainly because of security reasons. 

API has set of tools, definitions, and protocols for integrating application software and services. It lets your products and services communicate with other products and services without having to constantly build new connectivity infrastructure.

Choosing to share your APIs has several benefits, including:
•	Creating new revenue channels or extending existing ones.
•	Expanding the reach of your brand.
•	Facilitating open innovation or improved efficiency through external development and collaboration.

API requests consists of different components like HTTP method, HTTP header, GET method, POST method etc

About the API created in the Assignment:

The API in this assignment has been used to get various serialized AI models to solve question answering type problems.  First, we have used PUT method to get various model parameters from clients using POSTMAN. All the models are stored in the database created and can be retrieved using the GET method. Then, the client can request answers by providing ‘questions’ and ‘contexts.’ API uses POST method to get an answer.  

API location (for this assignment):

https://assgn2tag-isd4ai77qq-oa.a.run.app/

## 3. Dependencies!
    
### Torch: 
We used torch as a dependency for transformers

### Transformers: 
We used this dependency for answering question.


## 4. How to build and run the API locally via Docker or Flask
### Steps:
1. To build the API locally, I have used FLASK module in python. After imoporting the dependencines, a name "app" is given using Flask(__ name __). 
2. Now, on the base URL I have created different routes such as models and answer.  Models is to list, delete and add the models and answer is to get the answer on some context and question and list all the answered questions for a particular timestamp range.
3. For each route, I defined all the handlers/functions as per the methods mentioned in the route field. e.g. GET(to request the entire or filtered data), POST (to add new data), PUT(to modify the existing data) and DELETE (to delete data basis some query filter). 
4. Then, I used SQLite3 to create a database and tables. So that data can be inserted into these tables.
5. When everything is setup, I gave it a PORT number on which our flask can be run. 
6. Upon clicking on the given URL, I used this Flask app to get, put, post and delete any row from the database.     
