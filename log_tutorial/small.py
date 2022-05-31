
import log
logger = log.get_logger('small.log', 'small')

# logging.basicConfig(filename='small.log', format=' %(name)s %(levelname)s: %(message)s', level=logging.DEBUG)


def check_who_is_small(a, b):
    logger.info("Checking who is small ")
    if a>b:
        logger.debug("Result Found ")
        return a
    elif a<b:
        logger.debug("Result Found ")
        return a
    else:
        logger.error("Equal")
