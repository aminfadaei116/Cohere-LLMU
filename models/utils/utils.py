import json


def load_api_key():
    """
    load my cohere API key
    :return: str
    """
    with open('config.js') as config_file:
        config = json.load(config_file)
        api_key = config['api_key']
    return api_key
