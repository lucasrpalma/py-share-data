''' Module with the tables needed for the service '''

TABLES = {}

# ID without AUTO INCREMENT for this exercise purpose
TABLES['USERS'] = (
    """
    CREATE TABLE `users` (
        `ID` INT NOT NULL,
        `username` VARCHAR(255) NOT NULL,
        `role` VARCHAR(255) NOT NULL,
        `password` VARCHAR(255) NOT NULL,
        PRIMARY KEY (ID),
        UNIQUE (username)
        )
    """
)

TABLES['TOKENS'] = (
    """
    CREATE TABLE `tokens` (
        `ID` INT NOT NULL AUTO_INCREMENT,
        `token` VARCHAR(255) NOT NULL,
        `role` VARCHAR(255) NOT NULL,
        PRIMARY KEY (ID),
        UNIQUE (token)
        )
    """
)