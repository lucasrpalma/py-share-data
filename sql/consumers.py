''' Module for managing consumers with the DB '''
ADD_CONSUMER = "INSERT INTO consumers (ID, register_date, username, zip_code, credit_card, account_number, address, latitude, longitude, fav_color, doc_photo, ip_addr, car, car_model, car_type, car_color, purchases_number, avatar, birthday) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
