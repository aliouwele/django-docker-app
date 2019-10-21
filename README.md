# django-docker-app

Provide a ```Django|Python``` plateforme with docker

### Prerequisites

What things you need to install the software and how to install them

```
Docker
```
```
Git
```

### Installing

A step by step series of examples that tell you how to get a development env running

Clone the repository with git

```
git clone https://github.com/aliouwele/django-docker-app.git
```
Move to the folder
```
cd django-docker-app
```

And build docker images

```
docker-compose build
```
Run first the django app to create models ```OpenCelliD``` and apply these changes in our PostgreSQL database schema recognizes them and creates the necessary tables.

```
docker-compose up -d web
``` 
To create a admin account django backend.

```
 docker exec -it <Container ID> python manage.py createsuperuser
```

Run the app.

```
 docker-compose up
```
## View data in Django

To view the data imported into the database connect with admin account and go to the link: ```http://<ip>/admin/app/opencellid``` where ```ip``` is the server ip address (if local put localhost) or the docker machine ip address.  

### Running tests

Running unit tests

```
 docker exec -it <Container ID> python manage.py test
```

### Test REST API with curl

```curl``` is a ```command-line``` tool for transferring data and supports about 22 protocols including ```HTTP```. This combination makes it a very good ad-hoc tool for testing our ```REST services```. 

```
curl -v "http://<ip>/api/opencellid/?mcc=270&net=1&area=7007&cell=12386"
```

## Built With

* [Docker](https://docs.docker.com/) - Docker Container Monitoring
* [Pandas](https://pandas.pydata.org/pandas-docs/stable/) - Powerful ```Python``` data analysis toolkit
* [sqlalchemy](https://docs.sqlalchemy.org/en/13/) - The ```Python``` SQL Toolkit and Object Relational Mapper
* [Django](https://docs.djangoproject.com/en/2.2/) - ```Python``` Web Framework

 

## Authors

* **Aliou Samba WELE** - *Initial work* - [aliouwele](https://github.com/aliouwele)


## Acknowledgments

* Docker - Docker compose
* Pandas
* SqlAlchemy
* Django - Django Rest Framework
* PostgreSQL