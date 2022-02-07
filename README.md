# Crypto exchange information service

## Getting started
Setup environment configuration (create .env file in crypto_info module near settings.py).
At least you need setup ALPHAVANTAGE_EXCHANGE_API_KEY, all another values could be leave by default.

  <details>
    <summary><i><b>.env</b> example</i></summary>

  ```buildoutcfg
  POSTGRES_DB=crypto_info_db
  POSTGRES_USER=crypto_info_user
  POSTGRES_PASSWORD=crypto_info_password
  POSTGRES_HOST=postgresql
  POSTGRES_PORT=5432
  
  RABBITMQ_USER=guest
  RABBITMQ_PASSWORD=guest
  RABBITMQ_HOST=rabbitmq
  RABBITMQ_PORT=5672
  RABBITMQ_VHOST=/
    
  ALPHAVANTAGE_EXCHANGE_API_KEY=
  ```

  </details>

Start service:
```
docker-compose build
docker-compose run --rm app python manage.py migrate
docker-compose up
```
after this actions service will start and desired endpoint will be available:
http://127.0.0.1:8000/api/v1/quotes for methods: 
- GET: return last exchange rate for pair (BTC/USD)
  
- POST: force make request for get last exchange rate for pair (BTC/USD) from third party API (alphavantage).

##From author:
- I added extra technologies like Flower - its run in container with another services - so you could see call of celery tasks and result of execution there.
- I run celery beat and celery worker in different containers for more flexible usage.
- For POST method to endpoint /api/v1/quotes - I use .delay call of celery task  - as its call to external service and could be processed long time. 
  Also, I understood task - that this action only get the newest data from external API (and store it in DB) in parallel and return immediately response.
- For GET method there could be situation when table with "quotes" is empty - so I made response with the corresponding information. (For other behaviors - need a little discuss with)
- For interaction with 3-rd party API was used just function, which make request to it. In practice this functionality must be upgraded for usage different external services (functionality with same interface).
  Also - there are no handle any exceptions with 3-rd party API - which could be in real scenarios.
  

##SRS:
Write an API using Django that fetches the price of BTC/USD from the alphavantage
API every hour, and stores it on postgres. This API must be secured which means that
you will need an API key to use it. There should be two endpoints:
GET /api/v1/quotes - returns exchange rate and POST /api/v1/quotes which triggers
force requesting the prices from alphavantage. The API & DB should be
containerized using Docker as well.
- Every part should be implemented as simple as possible.
- The project should be committed to GitHub.
- The technologies to be used: Celery, Redis or RabbitMQ, Docker and Docker Compose.
- The sensitive data such as alphavantage API key, should be passed from the .env