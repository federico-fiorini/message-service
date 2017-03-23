###Message-service

Celery tasks to send messages through various channels (slack, emails).


#### How to run

	./start-docker-compose.sh
	
To update local image from latest remote docker image:

	./start-docker-compose.sh update

To update remote docker image:

    # Login with your docker username
    docker login
    
    # Build image from current directory (where Dockerfile is)
    docker build -t federicofiorini/message-service .
    
    # Push to repo
    docker push federicofiorini/message-service
