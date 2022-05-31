import log
logger = log.get_logger('big.log', 'big')


# logging.basicConfig(filename='big.log', format=' %(name)s %(levelname)s: %(message)s', level=logging.DEBUG)

def check_who_is_big(a, b):
    logger.info("Checking who is big ")
    if a>b:
        logger.debug("Result Found ")
        return a
    elif a<b:
        logger.debug("Result Found ")
        return a
    else:
        logger.error("Equal")
