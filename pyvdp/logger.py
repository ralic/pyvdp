import functools
import logging
import uuid

from pyvdp import configuration

config = configuration.get_config()


def get_logger():
    """Creates an instance of logger. See "Logging" chapter in docs for details.
    
    :return: logger 
    """
    logger = logging.getLogger('pyvdp')
    loglevel = logging.getLevelName(config['loglevel'])
    logger.setLevel(loglevel)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    if not logger.handlers:
        fh = logging.FileHandler(config['logfile'])
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger


def log_event(func):
    """Decorator function to log events."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = get_logger()

        result = func(*args, **kwargs)

        _uuid = uuid.uuid4()

        logger.info("[%s] Request: %s %s" % (_uuid, result['request']['method'], result['request']['url']))
        logger.debug("[%s] Request HTTP headers: %s" % (_uuid, result['request']['headers']))
        logger.debug("[%s] Request payload: %s" % (_uuid, result['request']['body']))

        logger.info("[%s] Response: HTTP %s" % (_uuid, result['response']['code']))
        logger.debug("[%s] Response HTTP headers: %s" % (_uuid, result['response']['headers']))
        logger.debug("[%s] Response message: %s" % (_uuid, result['response']['message']))

        return result

    return wrapper


def log_exception(func):
    """Decorator function to log exceptions."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = get_logger()

        result = kwargs['result']

        _uuid = uuid.uuid4()

        logger.error("[%s] Request: %s %s" % (_uuid, result['request']['method'], result['request']['url']))
        logger.debug("[%s] Request headers: %s" % (_uuid, result['request']['headers']))
        logger.debug("[%s] Request payload: %s" % (_uuid, result['request']['body']))

        logger.error("[%s] Response: HTTP %s" % (_uuid, result['response']['code']))
        logger.debug("[%s] Response headers: %s" % (_uuid, result['response']['headers']))
        logger.debug("[%s] Response message: %s" % (_uuid, result['response']['message']))

        func(*args, **kwargs)

    return wrapper
