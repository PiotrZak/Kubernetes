FROM tensorflow/serving

COPY ./2023-05-14 /models/2023-05-14

ENV MODEL_NAME 2023-05-14


# FROM python:3.8-slim-buster
# ENV PYTHONUNBUFFERED=1
# WORKDIR /app

# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# COPY . .

# EXPOSE 8501

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8501"]
