FROM python:3.8  

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy whole project to your docker home directory. 
COPY requirements.txt requirements.txt 
# run this command to install all dependencies  
RUN pip install -r requirements.txt  

COPY . .

# start server  
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

