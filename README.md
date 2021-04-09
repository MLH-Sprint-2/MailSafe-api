# MailSafe-api
![Djangobanner](https://user-images.githubusercontent.com/55349036/114230176-b65f0700-9970-11eb-8d99-fcd1c6cd23d2.png)
This is the Django RESTful API for MailSafe Application. The endpoints can be tested locally using PostMan with the endpoints provided below. The docker container uses the Alpine image.

![Djangobanner](https://user-images.githubusercontent.com/22732776/114239406-f7114d00-997d-11eb-8fc3-9a0fb46e83fc.png)


### Endpoints

### Running the application locally
1. Clone the Application
2. Start docker
3. Go to the folder containing docker container and execute `docker build .`
4. Now execute `docker-compose build` This should install all required packages and setup the container.
5. To start server use `docker-compose up` this should run server on localhost:8000
6. Now go to .env example and setup the environ variables as stated inside the file
7. To run normal Django commands through container use the following example `docker-compose run app sh -c "python manage.py migrate"       
`
