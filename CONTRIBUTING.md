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

# Docker compose

```
docker compose up --build --force-recreate --no-deps
```

# Stop the Docker Desktop
```
docker compose down -v
```

# psql command

```
PGPASSWORD=6dlwttqx9KLWpgZkrGJO5C0SKAdaLXsY psql -h dpg-cu1vn99opnds73aj9deg-a.oregon-postgres.render.com -U python_rest_api_db_user python_rest_api_db
```


# Database migrations

- First run the compose file with 
`docker compose up -d`

- Then run the database upgrade command with:
`docker compose exec web flask db upgrade`

$ flask db stamp head  # To set the revision in the database to the head, without performing any migrations. You can change head to the required change you want.
$ flask db migrate     # To detect automatically all the changes.
$ flask db upgrade     # To apply all the changes.