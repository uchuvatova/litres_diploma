import json
import os

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
SCHEMAS_PATH = os.path.join(PROJECT_ROOT_PATH, '../schemas')
STATUS_CART_PATH = os.path.join(SCHEMAS_PATH, 'status_cart.json')
SUCCESSFUL_REGISTER_USER_PATH = os.path.join(SCHEMAS_PATH, 'successful_register_user.json')
REGISTER_EXIST_USER_PATH = os.path.join(SCHEMAS_PATH, 'register_exist_user.json')
UNSUCCESSFUL_REGISTER_USER_PATH = os.path.join(SCHEMAS_PATH, 'unsuccessful_register_user.json')


def load_schema(filepath):
    with open(filepath) as file:
        schema = json.load(file)
        return schema
