import functools
import logging
import uuid


def get_logger():
    logger = logging.getLogger('pyvdp')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    if not logger.handlers:
        fh = logging.FileHandler('pyvdp.log')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger


def log_event(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = get_logger()

        result = func(*args, **kwargs)

        _uuid = uuid.uuid4()

        logger.info(_request_msg(_uuid, result['request']))
        logger.info(_response_msg(_uuid, result['response']))

        return result

    return wrapper


def log_exception(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = get_logger()

        result = kwargs['result']

        _uuid = uuid.uuid4()

        logger.error(_request_msg(_uuid, result['request']))
        logger.error(_response_msg(_uuid, result['response']))

        func(*args, **kwargs)

    return wrapper


def _request_msg(*args):
    return "[%s] Request: %s" % args


def _response_msg(*args):
    return "[%s] Response: %s" % args
