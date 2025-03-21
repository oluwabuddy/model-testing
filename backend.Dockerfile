FROM python:3.12-slim

WORKDIR /app/qa_interview

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000

VOLUME [ "/app/qa_interview" ]

CMD [ "fastapi", "dev", "api/main.py", "--host", "0.0.0.0" ]