# CONTRIBUTING

## How to run the docker file locally

```
docker build -t <IMAGE_NAME> .
```

```
MSYS_NO_PATHCONV=1 docker run -dp 5005:5000 -w /app -v $(pwd -W):/app <IMAGE_NAME> sh -c "flask run"
```

Or alternatively:
`docker compose -f docker-compose.yml -f docker-compose.debug.yml up`