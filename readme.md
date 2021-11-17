// Build the Docker image
docker build -t foodapi .

// Run the container
docker run -d -p 5000:5000 --name foodapi foodapi

// List the container
docker ps

// Logs
docker logs foodapi

// Exec into running container
docker exec -it foodapi /bin/sh