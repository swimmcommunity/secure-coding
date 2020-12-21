import yaml

CONFIGURATION_PATH = 'python/configuration.yaml'

def load_configuration():
    """
    >>> conf = load_configuration()
    >>> conf
    {'conf': {'key1': 'value1', 'api_key': 'ab'}}
    """
    with open(CONFIGURATION_PATH, 'r') as configuration_file:
        return yaml.safe_load(configuration_file.read())