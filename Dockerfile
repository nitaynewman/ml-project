# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY app.py app.py
COPY base_model.py base_model.py
COPY pklpredict.py pklpredict.py
COPY model/MODEL.pkl model/MODEL.pkl

RUN pip install --no-cache-dir -r requirements.txt

ENV MODEL_PATH=/app/model/MODEL.pkl

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
