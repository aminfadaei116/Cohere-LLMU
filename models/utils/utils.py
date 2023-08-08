import yaml


def load_api_key():
    """
    load my cohere API key
    :return: str
    """
    with open('config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)
        api_key = config['api_key']
    return api_key
