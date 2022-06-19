# Simple Data Sharing Project
## Introduction
This is a simple Python project exercise made to share data with some security and privacy controls.
It uses **Docker + Python/Flash + MySQL** stack.

## How to run
Simply use Docker Compose on root folder, as following:
> docker-compose -f docker-compose.yml up --build

After the initialization, you can perform a **GET** operation on **localhost** at **8000** port to double check that everything is up and running:
> curl http://localhost:8000/

## Features Implemented
- Simple authentication with "token" and "roles" usage
- Password storage with SHA512 and SALT
- Data consumption and storage in DB
- Different data sharing depending on the user role

## Improvements needed
- TLS
- Strong authentication protocol implementation (like OAUTH2)
- More user management features, as:
  - User registration
  - Password recovery
  - MFA
- Block the IP address and not the user
- Throttling on the requests (and firewall controls overall)
- Requests through WAF
- CI/CD with SAST, SCA, DAST and other security controls
- Better logging (including using **logging** instead of **print**)
- Docker image hardening
- External secrets service usage instead of hardcoded passwords