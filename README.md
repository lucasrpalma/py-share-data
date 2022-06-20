# Simple Data Sharing Project
## Introduction
This is a simple Python project exercise made to share data with some security and privacy controls.
It uses **Docker + Python/Flash + MySQL** stack.

## How to run
Simply use Docker Compose on root folder, as following:
> docker-compose -f docker-compose.yml up --build

After the initialization, you can perform a **GET** operation on **localhost** at **8000** port to double check that everything is up and running:
> curl http://localhost:8000/

## Debugging
### Debugging Data on the MySQL DB
If needed to enter the DB to check the data, you can use docker exec, as in:
> docker exec -it {MYSQL_CONTAINER_ID} mysql -u root -p 

*(**root** is the only user registered, it doesn't have more users, read replica, multi az, backups and other security controls)*

> When asked the password, use **@Py1234@** .

*(it's hardcoded on the code, as it doesn't have a secrets service, as it can be seen at the Improvements section, among others).*

After logging in the MySQL, the data will be on the **storage** DB:
> USE storage;

**Important**: The **storage** DB and the tables are only created and populated with default data before the first request. So, if the service is up and no request was made, there will be no data also.

### Debugging Logs on the Python application
For now, all the logs are being made with **print** instead of **logging** itself, with the Dockerfile configured to run Python unbuffered.
This decision was made to make it easier to debug directly on the terminal console, since it isn't a production environment. On regular applications it's better to use proper logging handling, with proper log library, protection on the files access, the file writing, check for log injection, among other protections.

## Features Implemented
- Simple authentication with "token" and "roles" usage
- Password storage with SHA512 and SALT
- Data consumption and storage in DB
- Different data sharing depending on the user role

## Improvements needed
- TLS
- Better authentication, as:
  - Strong authentication protocol implementation (like OAUTH2)
  - Better token management (incuding expiration)
  - Better cryptographic algorithms (maybe PBKDF2 instead of SHA512)
- More user management features, as:
  - User registration
  - Password recovery
  - Change password
  - MFA
  - Check for weak password
- Feature against brute force, as:
  - Block the user and/or the IP after a few tries
  - Throttling on the requests
- Requests through WAF and firewall overall
- CI/CD with SAST, SCA, DAST and other security controls
- Better logging (including using **logging** instead of **print**)
- Docker image hardening
- External secrets service usage instead of hardcoded passwords
- Check for long inputs trying to make a DoS
- Better testing against concurrency issues
- Better error handling
- Unit and integrations tests