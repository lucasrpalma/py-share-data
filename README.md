# Simple Data Sharing Project
## Introduction
This is a simple Python project exercise made to share data with some security and privacy controls.
It uses **Docker + Python/Flash + MySQL** stack.

It was made to solve a problem on how to share data in a secure way.
In this case, the idea is to have a login authentication with tokens and role based users. This way, the data being shared is differently according to the role of the user requesting it.

The scope was considered as an internal application for a Fintech (but not a card issuer, so no CVV allowed). This application is responsible to sharing the data to other employees and/or services, but the correct amount of data would be shared according to the user role.

A few documents so you can better understand the application.

## Documents Index
1. [How to run](docs/01%20-%20HOW%20TO%20RUN.md)
2. [Debug](docs/02%20-%20DEBUG.md)
3. [Tutorial](docs/03%20-%20TUTORIAL.md)
4. [Features](docs/04%20-%20FEATURES.md)
5. [Improvements needed](docs/05%20-%20IMPROVEMENTS%20NEEDED.MD)
6. [Application description](docs/06%20-%20APPLICATION%20DESCRIPTION.MD)

## Few drawbacks

Although a few security controls were made (as authentication with token usage, password storage with hash and salt), other basic ones aren't made (TLS implementation, OAUTH2, among others) as they were considered out of scope.

Also, no private nor secret data is exposed through logs, but they're stored clean at the database. On real case scenario, it would be better to have better permissioning on the database (for example, secret/private/financial data on different schema with different permissions). Another good option is to use cryptography on some of the data, storing the key on a separate and secure place (as a KMS).

Another topic is that ideally the credit card isn't stored, but a tokenization is made with the card issuer and just the token is stored. Since here we have only the card, not the token, the card itself was stored considering that it would be used later and considering that it's a financial company with proper use and handling for them (but the CVV wasn't stored, since it wasn't considered that the company is a card issuer). At transit, the card doesn't appear in logs and, for regular users, a mask was used so only the needed digits are shown.

A lot more issues and improvements can be seen on [Section 5, Improvements Needed](/docs/05%20-%20IMPROVEMENTS%20NEEDED.MD).
Also, a [Risk Register](docs/Risk%20Register.xlsx) was made containing a more detailed view of some important risks identified on the application, with rating and mitigation plan.