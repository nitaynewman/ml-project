# Dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /code

COPY ./app /code/app
COPY ./model /code/model

RUN pip install --no-cache-dir --upgrade -r /code/app/requirements.txt

CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "80"]
