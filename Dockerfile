# #Specifying the base image
# FROM python:3.8.8
# #here the dockerfile is pulling the python 3.8.8 from docker hub which already has python installed so we have all the things we need to have python in our container.

# ADD main.py .
# #Here we added the python file that we want to run in docker and define its location.

# # RUN pip install requests pygame
# #Here we installed the dependencies, we are using the pygame library in our main.py file so we have to use the pip command for installing the library

# CMD ["python3","./main.py"]
# #lastly we specified the entry command this line is simply running python ./main.py in our container terminal

FROM python:3.7-slim

ENV PYTHONUNBUFFERED True
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install Flask gunicorn

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app