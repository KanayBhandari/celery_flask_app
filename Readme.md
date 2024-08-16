# Setup to run celery with flask (using RabbitMQ)

You will need RabbitMQ installed in your system for this.

### RabbitMQ
RabbitMQ is built on Erlang runtime so before installing RabbitMQ, we need to download Erlang and install it.
* Erlang
* RabbitMQ

Follow this guide to install **RabbitMQ**
https://www.tutorialspoint.com/rabbitmq/rabbitmq_installation.htm


### Run the setup locally

1. Create python virtual env and install requirements inside it.

`python -m venv venv`

2. Activate the virtual env based on your OS

`source venv/bin/activate (Linux)`

`source venv/Scripts/activate (Windows)`

3. Install the requirements:

`pip install -r requirements.txt`

4. Create a .env file at the root of your directory and
add below entries to it.

```
USER=guest
PASSWORD=guest
```


5. Open different terminals to run various things:
* flask app
* celery worker
* celery beat (scheduler)
* flower (open source web app for monitoring and managing celery clusters, it provides real time information about the status of Celery workers and tasks)

### Flask App

Execute the commands in Git Bash terminal

* export FLASK_APP=proj.app
* export FLASK_ENV=development
* flask run

### Celery Worker

Remember if you are in windows you need to run the worker command with `--pool=solo`

* celery -A proj.celery:celery worker --loglevel=INFO --pool=solo

### Celery Beat (Scheduler)

* celery -A proj.celery:celery beat --loglevel=INFO


### Flower

Flower is a real-time web application monitoring and administration tool for Celery.

* celery -A proj.celery:celery flower

local access url: http://localhost:5555/

#### To test the flask API you can run the below command in another terminal


curl localhost:5000/user/ping

After this monitor the response in the terminal where celery worker is running it will execute the task defined in api in the celery worker.

