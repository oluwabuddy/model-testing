FROM python:3.12-slim

WORKDIR /app/qa_interview

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8001

VOLUME [ "/app/qa_interview" ]

CMD [ "streamlit", "run", "frontend/Model.py", "--server.port", "8001", "--server.address", "0.0.0.0" ]