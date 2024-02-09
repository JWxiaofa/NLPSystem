# Assignment 1

The code assumes Python version 3.8 or higher.


### FastAPI

To run:

```bash
$ uvicorn app_fastapi:app --reload
```

Then open another terminal to access the API:

```bash
$ curl http://127.0.0.1:8000
# NER
$ curl -X POST http://127.0.0.1:8000/ner \
       -H 'accept: application/json' \
       -H 'Content-Type: application/json' \
       -d@input.json 
# Dependency parsing
$ curl -X POST http://127.0.0.1:8000/dep \
       -H 'accept: application/json' \
       -H 'Content-Type: application/json' \
       -d@input.json        
```
To set prerry to true:
```bash
$ curl 'http://127.0.0.1:8000?pretty=true'
$ curl -X POST 'http://127.0.0.1:8000/ner?pretty=true' \
       -H 'accept: application/json' \
       -H 'Content-Type: application/json' \
       -d@input.json 
$ curl -X POST 'http://127.0.0.1:8000/dep?pretty=true' \
       -H 'accept: application/json' \
       -H 'Content-Type: application/json' \
       -d@input.json 
```

### Flask server

To run:

```bash
$ python app_flask.py
```

To access the website point your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000). 


### Streamlit

To run:

```bash
$ streamlit run app_streamlit.py
```
