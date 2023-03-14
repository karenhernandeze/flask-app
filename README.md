# Simple Login App Using Flask and Docker

## Set Up & Installation.

### 1. 

    git clone https://github.com/karenhernandeze/flask-app.git
    cd flask-app

### 2. 

    docker build --tag python-docker .

### 3. 

    docker run -d -p 5000:5000 python-docker
    
### 4. 

    Visit link http://localhost:5000/

### 5. To stop the currently running container, we execute this command:

    docker ps (To get docker containers info) 
    docker stop <container-name>

