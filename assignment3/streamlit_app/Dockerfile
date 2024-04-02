FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install spacy && \
    python -m spacy download en_core_web_sm
EXPOSE 8501
CMD ["streamlit", "run", "app_streamlit.py"]