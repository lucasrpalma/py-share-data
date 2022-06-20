''' Utils library for general functions '''
import json
import sys
sys.path.append('../sql')
from sql.users import ROLES


def get_consumer(consumer, role):
    ''' Function to get the consumer data according to given role '''
    # General data
    consumer_dict = {}
    consumer_dict["id"] = consumer.ID
    consumer_dict["fec_alta"] = consumer.register_date
    consumer_dict["user_name"] = consumer.username
    consumer_dict["auto"] = consumer.car
    consumer_dict["auto_modelo"] = consumer.car_model
    consumer_dict["auto_tipo"] = consumer.car_type
    consumer_dict["auto_color"] = consumer.car_color
    consumer_dict["cantidad_compras_realizadas"] = consumer.purchases_number
    consumer_dict["avatar"] = consumer.avatar
    # Private data
    if role in (ROLES['ADMIN'], ROLES['PRIVACY']):
        consumer_dict["codigo_zip"] = consumer.zip_code
        consumer_dict["direccion"] = consumer.address
        consumer_dict["geo_latitud"] = consumer.latitude
        consumer_dict["geo_longitud"] = consumer.longitude
        consumer_dict["color_favorito"] = consumer.fav_color
        consumer_dict["foto_dni"] = consumer.doc_photo
        consumer_dict["ip"] = consumer.ip_addr
        consumer_dict["fec_birthday"] = consumer.birthday
    # Financial data
    if role in (ROLES['ADMIN'], ROLES['FINANCE']):
        consumer_dict["credit_card_num"] = consumer.credit_card
        consumer_dict["cuenta_numero"] = consumer.account_number
    json_result = json.dumps(consumer_dict)
    return json_result
