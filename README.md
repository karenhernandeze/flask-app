# Simple Login App Using Flask and Docker

## Set Up & Installation.

### 1. 

    git clone https://github.com/karenhernandeze/flask-app.git
    cd flask-app

### 2. 

    docker build --tag python-docker .

### 3. 

    docker run -d -p 5000:5000 python-docker

### 4. To stop the currently running container, we execute this command:

    docker stop <container-name>

