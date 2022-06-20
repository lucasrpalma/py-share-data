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

# CVV is never stored if not an issuer
TABLES['CONSUMERS'] = (
    """
    CREATE TABLE `consumers` (
        `ID` INT NOT NULL,
        `register_date` VARCHAR(255),
        `username` VARCHAR(255),
        `zip_code` VARCHAR(255),
        `credit_card` VARCHAR(255),
        `account_number` VARCHAR(255),
        `address` VARCHAR(255),
        `latitude` VARCHAR(255),
        `longitude` VARCHAR(255),
        `fav_color` VARCHAR(255),
        `doc_photo` VARCHAR(255),
        `ip_addr` VARCHAR(255),
        `car` VARCHAR(255),
        `car_model` VARCHAR(255),
        `car_type` VARCHAR(255),
        `car_color` VARCHAR(255),
        `purchases_number` VARCHAR(255),
        `avatar` VARCHAR(255),
        `birthday` VARCHAR(255),
        PRIMARY KEY (ID)
        )
    """
)