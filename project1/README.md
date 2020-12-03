#Project 1
This can be tested via postman
or
flasgger - pip install flasgger

Get call using URL like something below
http://127.0.0.1:5000/predict?var=2&skew=3&curt=-1&entr=4

app.run(host='0.0.0.0',port=8001)

Base Image - python:3
```
FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "./app.py" ]
```
Base Image - Anaconda3
```
FROM continuumio/anaconda3
WORKDIR /usr/app/
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "./app.py" ]
```