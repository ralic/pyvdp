import os

try:
    import configparser as parser
except ImportError:
    import ConfigParser as parser

DEFAULT_CONFIG = {
    'url': 'https://sandbox.api.visa.com',
    'username': '',
    'password': '',
    'version': 'v1',
    'cert': '',
    'key': '',
    'loglevel': 'ERROR',
    'logfile': 'pyvdp.log',
    'shared_secret': '',
    'api_key': ''
}


def get_config(config_path=None):
    """Validates configuration file.

    :param config_path: **Optional**. Full path to configuration file including filename. Default is PYVDP_CONFIG env
        variable value or `configuration.ini` file in current directory. 
    :return: configuration
    """
    if not config_path:
        config_path = os.getenv('PYVDP_CONFIG', os.path.join(os.path.dirname(__file__), 'configuration.ini'))

    # config file existence
    if not os.path.exists(config_path):
        message = "Could not find configuration file in %s. " \
                  "See \"Configuration\" chapter in docs for details." % config_path
        raise VisaConfigurationError(message)

    config = parser.ConfigParser()
    config.read(config_path)

    configuration = DEFAULT_CONFIG
    config_dict = dict(config.items('VISA'))

    configuration.update(config_dict)

    return configuration


class VisaConfigurationError(Exception):
    """Raised with invalid configuration"""
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
