# MailSafe-api
![Djangobanner](https://user-images.githubusercontent.com/55349036/114230176-b65f0700-9970-11eb-8d99-fcd1c6cd23d2.png)
This is the Django RESTful API for MailSafe Application. The endpoints can be tested locally using PostMan with the endpoints provided below. The docker container uses the Alpine image.

![Djangobanner](https://user-images.githubusercontent.com/22732776/114239406-f7114d00-997d-11eb-8fc3-9a0fb46e83fc.png)


### Endpoints

NOTE ALL ENDPOINTS ARE RESTRICTED VIA Authenticated Header 

Authorization : Token <a85efc83ccb629878a4d6d15e1fc1ffb51136da9> --> Example
All payload i s of raw json type
  
Access Admin panel via browser directly
```
admin/
```
Access to domains
```
alias/<str:DOMAIN>'
```
Login token requires payload

```
/auth/users/token/email/


payload
{
"username": "admin",
"password": "123"
}

response

{
"token": "",
"user_id": ""
}

```

Delete
```
v1/domains/:domain/aliases/:id
```
Domains
```
def get_alias_filtered(request, DOMAIN):
    """
    Return Domain filtered by domain
    API_ENDPOINT:api/v1/alias/<domains>
    Json raw body 
    ---------------
    Auth will be header with key Authorization : Token a85efc83ccb629878a4d6d15e1fc1ffb51136da9
    {
    "name": "432",
    "recipients": "random@email.com",
    "is_enabled": true
    }
```



### Running the application locally
1. Clone the Application
2. Start docker
3. Go to the folder containing docker container and execute `docker build .`
4. Now execute `docker-compose build` This should install all required packages and setup the container.
5. To start server use `docker-compose up` this should run server on localhost:8000
6. Now go to .env example and setup the environ variables as stated inside the file
7. To run normal Django commands through container use the following example `docker-compose run app sh -c "python manage.py migrate"`


