import pytest
from restapi_final import create_app
import time
import sqlite3
timestamp = int(time.time())

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    #Create in memory sqlite db
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    # test_db = SQLAlchemy(app)
    with app.test_client() as client:
        yield client

def test_health(client):
    r = client.get("/")
    assert 200 == r.status_code


def test_addModel(client):
    print("Testing Add Model functionality")
    # Test add a model functionality
    payload = {
        "name": "bert-tiny",
        "tokenizer": "mrm8488/bert-tiny-5-finetuned-squadv2",
        "model": "mrm8488/bert-tiny-5-finetuned-squadv2"
    }
    r = client.put("/models", json=payload)
    assert 200 == r.status_code

def test_getModel(client):
    # test /models GET
    r = client.get("/models")
    assert 200 == r.status_code

def test_postAnswer(client):
    # Test /answer POST
    payload = {
        "question": "What is the capital city of Indiana?",
        "context": "Indianapolis, colloquially known as Indy, is the state capital and most-populous city of the U.S. state of Indiana and the seat of Marion County. According to 2019 estimates from the U.S. Census Bureau, the consolidated population of Indianapolis and Marion County was 886,220."
    }
    headers = {
        'Content-Type': 'application/json'
    }
    model_string = ['?model=distilled-bert', '']
    for m in model_string:
        r = client.post("/answer" + m, json=payload, headers=headers)
        assert 200 == r.status_code


def test_getAnswer(client):
    # Test /answer GET
    query_string = ["?model=bert-tiny&start="+timestamp+"&end="+timestamp, "?start="+timestamp+"&end="+timestamp]
    for q in query_string:
        r = client.get("/answer" + q)
        assert 200 == r.status_code

def test_deleteModel(client):
    # Test /models DELETE
    r = client.delete("/models?model=bert-tiny")
    assert 200 == r.status_code


if __name__ == '__main__':
    timestamp = int(time.time())
    # Connect to database
    conn = sqlite3.connect("test_db.db")
    # Create a cursor
    c = conn.cursor()
    # Create a table
    c.execute("""CREATE TABLE IF NOT EXISTS models (
                name varchar(100), tokenizer varchar(100), model varchar(100)
        )""")
    c.execute("""CREATE TABLE IF NOT EXISTS answers (
                timestamp DateTime, model varchar(100), answer varchar(500), question varchar(500), context varchar(500)
        )""")
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(c.fetchall())
    # commit and close
    conn.commit()
    conn.close()
