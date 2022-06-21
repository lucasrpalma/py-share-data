# Debug
## Debugging Data on the MySQL DB
If needed to enter the DB to check the data, you can use docker exec, as in:
> docker exec -it {MYSQL_CONTAINER_ID} mysql -u root -p 

*(**root** is the only user registered, it doesn't have more users, read replica, multi az, backups and other security controls)*

> When asked the password, use **@Py1234@** .

*(it's hardcoded on the code, as it doesn't have a secrets service, as it can be seen at the Improvements section, among others).*

After logging in the MySQL, the data will be on the **storage** DB:
> USE storage;

**Important**: The **storage** DB and the tables are only created and populated with default data before the first request. So, if the service is up and no request was made, there will be no data also.

## Debugging Logs on the Python application
For now, all the logs are being made with **print** instead of **logging** itself, with the Dockerfile configured to run Python unbuffered.
This decision was made to make it easier to debug directly on the terminal console, since it isn't a production environment. On regular applications it's better to use proper logging handling, with proper log library, protection on the files access, the file writing, check for log injection, among other protections.