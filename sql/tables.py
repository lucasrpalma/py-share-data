TABLES = {}

TABLES['USERS'] = (
    """
    CREATE TABLE `users` (
        `ID` INT NOT NULL AUTO_INCREMENT,
        `username` VARCHAR(255) NOT NULL,
        `role` VARCHAR(255) NOT NULL,
        `password` VARCHAR(255) NOT NULL,
        PRIMARY KEY (ID)
        )
    """
)