import os

from pyvdp.exceptions import VisaConfigurationError

try:
    import configparser as parser
except ImportError:
    import ConfigParser as parser


def get_config(config_path):
    """Validates configuration file.

    :param config_path: Full path to configuration file including filename
    :return: configuration
    """
    # config file existence
    if not os.path.exists(config_path):
        message = "Could not find configuration file in %s. " \
                  "See \"Configuration\" chapter in docs for details." % config_path
        raise VisaConfigurationError(message)

    config = parser.ConfigParser()
    config.read(config_path)

    # required params
    try:
        configuration = {
            'url': config.get('VISA', 'url'),
            'version': config.get('VISA', 'version'),
        }
    except parser.NoSectionError as e:
        raise VisaConfigurationError("PyVDP configuration error: %s in %s" % (e.message, config_path))
    except parser.NoOptionError as e:
        raise VisaConfigurationError("PyVDP configuration error: %s in %s" % (e.message, config_path))

    # username and password
    try:
        configuration.update({
            'username': config.get('VISA', 'username'),
            'password': config.get('VISA', 'password'),
        })
    except parser.NoOptionError:
        configuration.update({
            'username': '',
            'password': '',
        })

    # Certificate and keyfile
    try:
        config_dir = os.path.dirname(config_path)

        cert_path = os.path.join(config_dir, config.get('VISA', 'cert'))
        key_path = os.path.join(config_dir, config.get('VISA', 'key'))

        # Validate certificate and keyfile
        if not os.path.exists(cert_path):
            message = "Could not find certificate file in %s" % cert_path
            raise VisaConfigurationError(message)
        elif not os.path.exists(key_path):
            message = "Could not find keyfile in %s" % key_path
            raise VisaConfigurationError(message)

        configuration.update({
            'cert': cert_path,
            'key': key_path,
        })
    except parser.NoOptionError:
        configuration.update({
            'cert': '',
            'key': '',
        })

    # shared secret and api key
    try:
        configuration.update({
            'shared_secret': config.get('VISA', 'shared_secret'),
            'api_key': config.get('VISA', 'api_key'),
        })
    except parser.NoOptionError:
        configuration.update({
            'shared_secret': '',
            'api_key': '',
        })

    # logging

    try:
        configuration.update({
            'logfile': config.get('LOGGING', 'logfile'),
        })
    except (parser.NoSectionError, parser.NoOptionError):
        configuration.update({
            'logfile': 'pyvdp.log',
        })

    try:
        configuration.update({
            'loglevel': config.get('LOGGING', 'loglevel')
        })
    except (parser.NoSectionError, parser.NoOptionError):
        configuration.update({
            'loglevel': 'ERROR'
        })

    return configuration

