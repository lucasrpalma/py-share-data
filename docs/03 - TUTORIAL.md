# Tutorial
A simple tutorial to guide you through the application.

## Initializing the data
There's no need to initialize the data. It's already configured that, before the first request, it'll be done automatically.
That also makes that the first request of all after starting the application is longer than usual.
We recommend to begin with the **Healthcheck** request since it's the fastest one.

## Healthcheck
Simply make a **GET request** on the root URL to check if everything is fine: `http://localhost:8000/`

It should return a JSON stating that it is working:
```
{
    'Message':'It works!'
}
```

## Login
You can login with 4 different users, each one has each own role:
| User | Password | Role |
| ---- | -------- | ---- |
| admin | admin123 | superuser |
| dpo | dpo123 | privacy |
| payment | payment123 | finance |
| user | user123 | common |

Each role gives access to a different set of data, as it can be seen following on:
| Role | Privacy Data | Financial Data | Other Data |
| ---- | ------------ | -------------- | ---------- |
| superuser | Yes | Yes | Yes |
| privacy | Yes | Masked | Yes |
| finance | No | Yes | Yes |
| common | No | Masked | Yes |

>The data is fully stored on the database (except from CVV), but it's considered that each user can access only the set according to their role.
>> The CVV should NEVER be stored, unless you're a card issuer (which isn't the scope of this problem). It's considered that, if the user wants the CVV from the user, he/she will ask for it during the transaction.

To log in, you have to send a **POST request** on `http://localhost:8000/login` with the following body:
```
{
    "username": "user",
    "password": "password"
}
```

For example, to log in with the admin, you use the following body:
```
{
    "username": "admin",
    "password": "admin123"
}
```

If everything goes well, it'll return a token, as for example:
```
{
    'token':'e0ac1c87-55e7-4188-8a4e-8ea34abb05e3'
}
```

Keep it because it'll be needed for the next request.

## Querying data
On this exercise you can query the data from one of the consumers that are on the consumers list from the mock service.
This service allows you to query it using either the consumer **ID** or his/her **username**.
> If both **ID** and **username** are provided, only the ID will be considered.

To perform the query, you need to make a **GET request** on the `consumer` route and using *id* or *username* as query parameters.
So, the request would be: `http://localhost:8000/consumer?id=` or `http://localhost:8000/consumer?username=`.
Here are a few examples:
```
http://localhost:8000/consumer?id=2
```

```
http://localhost:8000/consumer?username=Ethelyn.Schinner
```

Now, if you try to make the request, an error should appear, like this:
```
{
    'Error':'Invalid authentication token'
}
```

This is beacause the data is only available if you're logged in.
Do you remember the token from the [Login](#login) right? Now is the time to use it.
Set the following header:
```
token: token-provided
```

For example:
```
token: dd72a234-988f-4b71-a890-dc7fd1801498
```

> A full cURL command with all of this would look like:
> ```
> curl --location --request GET 'http://localhost:8000/consumer?id=2' \
> --header 'token: dd72a234-988f-4b71-a890-dc7fd1801498'
> ```

With this request and the token, you should be able to receive the data on JSON format.
For a **regular user** querying the **id=2** you would receive:
```
{
    "id": 2,
    "fec_alta": "2021-07-31T00:11:06.741Z",
    "user_name": "Junior39",
    "auto": "Bugatti Corvette",
    "auto_modelo": "Challenger",
    "auto_tipo": "Cargo Van",
    "auto_color": "Lamborghini PT Cruiser",
    "cantidad_compras_realizadas": "30564",
    "avatar": "https://cdn.fakercloud.com/avatars/franciscoamk_128.jpg",
    "credit_card_num": "6767-22**-****-5169",
    "cuenta_numero": "50****04"
}
```

Meanwhile, the same request for an **admin** will receive:
```
{
    "id": 2,
    "fec_alta": "2021-07-31T00:11:06.741Z",
    "user_name": "Junior39",
    "auto": "Bugatti Corvette",
    "auto_modelo": "Challenger",
    "auto_tipo": "Cargo Van",
    "auto_color": "Lamborghini PT Cruiser",
    "cantidad_compras_realizadas": "30564",
    "avatar": "https://cdn.fakercloud.com/avatars/franciscoamk_128.jpg",
    "codigo_zip": "22139",
    "direccion": "Amelia Forks",
    "geo_latitud": "-40.0728",
    "geo_longitud": "-39.5073",
    "color_favorito": "white",
    "foto_dni": "http://placeimg.com/640/480",
    "ip": "224.140.175.223",
    "fec_birthday": "2022-03-29T03:28:16.364Z",
    "credit_card_num": "6767-2293-4172-5169",
    "cuenta_numero": "50099904"
}
```

For a **financial** user:
```
{
    "id": 2,
    "fec_alta": "2021-07-31T00:11:06.741Z",
    "user_name": "Junior39",
    "auto": "Bugatti Corvette",
    "auto_modelo": "Challenger",
    "auto_tipo": "Cargo Van",
    "auto_color": "Lamborghini PT Cruiser",
    "cantidad_compras_realizadas": "30564",
    "avatar": "https://cdn.fakercloud.com/avatars/franciscoamk_128.jpg",
    "credit_card_num": "6767-2293-4172-5169",
    "cuenta_numero": "50099904"
}
```

And finally, for a **privacy** user:
```
{
    "id": 2,
    "fec_alta": "2021-07-31T00:11:06.741Z",
    "user_name": "Junior39",
    "auto": "Bugatti Corvette",
    "auto_modelo": "Challenger",
    "auto_tipo": "Cargo Van",
    "auto_color": "Lamborghini PT Cruiser",
    "cantidad_compras_realizadas": "30564",
    "avatar": "https://cdn.fakercloud.com/avatars/franciscoamk_128.jpg",
    "codigo_zip": "22139",
    "direccion": "Amelia Forks",
    "geo_latitud": "-40.0728",
    "geo_longitud": "-39.5073",
    "color_favorito": "white",
    "foto_dni": "http://placeimg.com/640/480",
    "ip": "224.140.175.223",
    "fec_birthday": "2022-03-29T03:28:16.364Z",
    "credit_card_num": "6767-22**-****-5169",
    "cuenta_numero": "50****04"
}
```

## Conclusion
With this exercise it was possible to check some security controls that can be used to make the data more secure, as a role based login to share the correct amount of data for each type of user.

Much more is needed to have a strong security on the whole application and infrastructure, as it can be seen on [Improvements needed](05%20-%20IMPROVEMENTS%20NEEDED.MD) document, but they were considered out of the scope of the issue given.
On real case scenario there are many teams and services, with different responsibilites, which would work together (hopefully!) to make a stable and secure application for the end user.