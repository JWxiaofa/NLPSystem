FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install spacy && \
    python -m spacy download en_core_web_sm
EXPOSE 8000
CMD ["uvicorn", "app_fastapi:app", "--host=0.0.0.0", "--reload"]