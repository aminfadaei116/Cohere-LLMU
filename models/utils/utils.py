import yaml


def load_api_key() -> str:
    """
    load my cohere API key
    :return: str
        The api string that allows us to use the Cohere API
    """
    with open('api_key.yml', 'r') as config_file:
        config = yaml.safe_load(config_file)
        api_key = config['api_key']
    return api_key




