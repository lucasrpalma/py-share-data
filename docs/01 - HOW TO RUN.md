# How to run
Simply use Docker Compose on root folder, as following:
> docker-compose -f docker-compose.yml up --build

After the initialization, you can perform a **GET** operation on **localhost** at **8000** port to double check that everything is up and running:
> curl http://localhost:8000/

# Tutorial
On the [Tutorial section](03%20-%20TUTORIAL.md) you can find more on how to use the application.

## Postman collection
If you think it easier to use Postman to make your requests, there's a **Postman Collection** on this repository, here at **docs folder**, or simply on this [link](PyShareData-PostmanCollection.json). You can download and import it to your JSON, to automatically create a collection with the requests needed and the environment for token usage.

It's already configured to make the following requests:
- Healthcheck
- Login as each user
- Consumer search by ID with each user
- Consumer search by username with each user

It's also configured to automatically get the token on login and use it on the request.
> If you're going to use it, we still **highly recommend to read the tutorial** together with it, to understand better each request and each feature.