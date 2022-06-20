''' Module to get the external content and store in the DB '''
import requests
from consumer import Consumer
from libs import utils
import db

def get_external_data():
    ''' Function to get the data from the Mock server '''
    url = 'https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios'
    get_data = requests.get(url)
    if get_data.status_code == 200:
        data = get_data.json()
        consumers_list = []
        for consumer_data in data:
            consumers_list.append(
                Consumer(consumer_data["id"],
                        consumer_data["fec_alta"],
                        consumer_data["user_name"],
                        consumer_data["codigo_zip"],
                        consumer_data["credit_card_num"],
                        consumer_data["cuenta_numero"],
                        consumer_data["direccion"],
                        consumer_data["geo_latitud"],
                        consumer_data["geo_longitud"],
                        consumer_data["color_favorito"],
                        consumer_data["foto_dni"],
                        consumer_data["ip"],
                        consumer_data["auto"],
                        consumer_data["auto_modelo"],
                        consumer_data["auto_tipo"],
                        consumer_data["auto_color"],
                        consumer_data["cantidad_compras_realizadas"],
                        consumer_data["avatar"],
                        consumer_data["fec_birthday"]
            ))
        db.insert_new_consumer_list(consumers_list)
    else:
        print('Error getting data from mock server')
