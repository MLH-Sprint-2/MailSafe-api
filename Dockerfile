FROM python:3.7-alpine
MAINTAINER Sachin_Lucas_Apratim
# recommended to run with this in docker container 
ENV PYTHONUNBUFFERED 1
# Dependencies from requirement.txt -> docker
COPY ./requirements.txt /requirements.txt
# run pip on it
RUN pip install -r requirements.txt

# -----------------------------------
#Application source code here 
RUN mkdir /app 
# This will be the working directory -> this will be staring
# directory
WORKDIR /app 
# copy the code dev writes into docker
COPY ./app /app 

# ------------------------------------
# Create user that will run the app using docker
# -D means user can only run project not admin
RUN adduser -D user
# Switch user to user we created
# prevents the user from having root access and have only
# access to our application in our container
USER user