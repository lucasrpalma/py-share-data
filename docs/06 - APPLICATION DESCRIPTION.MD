# Application Description
On this section it is described what each Python script does and how they work.

# Root folder
The folder with the main business functions needed by the application.

## APP.PY
It's the main application. Contains the flask server and the routes needed for the requests to be made.
It also calls the functions needed for each requests, handling the response accordingly.

## AUTH.PY
Contains the authentication features. In this case, there are two functions:
- **Login**: If the login and password matches from a user in the DB, it'll generate a new token using UUID and return it. If not, it'll return an error code according to HTTP STATUS CODE.
> PS: It returns different errors for user not found and wrong password for debugging purpose. The application returns the same error for the user on both cases, to make it more difficult for an attacker to perform an enumeration attack.

- **Get Role**: It'll receive a token, check if it's valid and, if postive, will return the role associated to it.

## CONSUMER.PY
Contains a class to handle a consumer. On this exercise, a consumer is one of the many items from the JSON array that the Mock service returns.

## DB.PY
Performs all the queries within the DB.
The queries that receive parameters are using Prepared Statement.

## EXTERNALCONTENT.PY
It gets the data from the Mock service and store it _(except from the CVV)_ on the database.

# LIBS folder
The folder containing some functions to support the main application.

## CRYPTO.PY
Related to the cryptographic functions. For now, it contains only the function to hash the password using SHA512.

## UTILS.PY
It contains some extra functions to better handle the Consumer. It enables the application to get a consumer from the database and print it differently according to the user's role.

# SQL folder
Contains the variables with the SQL queries.

## CONSUMERS.PY
Queries related to the Consumers table.

## TABLES.PY
Queries to create all the tables.

## TOKENS.PY
Queries related to the Tokens table.

## USERS.PY
Queries related to the Users table.

# Application Diagram
A diagram was made with the relationship between the application modules.
![Application Diagram](06%20-%20MODULES%20DIAGRAM.png "Application Diagram")