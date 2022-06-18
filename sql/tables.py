''' Module with the tables needed for the service '''

TABLES = {}

TABLES['USERS'] = (
    """
    CREATE TABLE `users` (
        `ID` INT NOT NULL,
        `username` VARCHAR(255) NOT NULL,
        `role` VARCHAR(255) NOT NULL,
        `password` VARCHAR(255) NOT NULL,
        PRIMARY KEY (ID)
        )
    """
)
