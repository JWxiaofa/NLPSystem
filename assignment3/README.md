# Assignment 3

The code assumes Python version 3.8 or higher.

## Docker Image and Container
There are three docker images for flask, FastAPI and streamlit separately. To create the image, make sure Docker is installed,
and then `cd` to `assignments/assignment3` directory, and then run the command:

```bash
$ docker-compose build
```

Then, run the following command to run the container:

```bash
$ docker-compose up
```

You can then access the three servers at the same time.

Flask server: http://127.0.0.1:5001 

FastAPI: http://0.0.0.0:8000

Streamlit: http://127.0.0.1:8501 or http://localhost:8501
