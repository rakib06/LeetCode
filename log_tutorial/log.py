import logging



def get_logger(filename, name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.ERROR)

    formater = logging.Formatter('%(name)s: %(levelname)s: %(message)s')
    file_handler = logging.FileHandler(filename)
    file_handler.setFormatter(formater)

    logger.addHandler(file_handler)
    return logger