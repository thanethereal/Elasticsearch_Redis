## What is it:

SOLID Async API for online cinema with no registration.  

## What is in it:

1. SOLID async API to get data about movies, genres, persons
2. Covering tests with pytest
3. Added API requests check. Valid JWT-token from Auth-servce is needed.
4. Added graceful degradation: JWT-tokens' ttl to be increased by MAX_ADDITIONAL_TIME to let Auth service recover.

## How to start:

docker-compose up -d --build 
(You may need data in Elasticsearch to see how it works)

## Documentation:

http://0.0.0.0:8000/api/openapi

## How to test:

docker-compose -f docker-compose.yml -f docker-compose.tests.yml up --build

## Stack:

Async FastAPI, Elasticsearch, Docker Compose, Redis, Nginx, pytest
