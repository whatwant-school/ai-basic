import logging

if __name__ == '__main__':
    logger = logging.getLogger("main")
    logging.basicConfig(level=logging.DEBUG)
    logger.setLevel(logging.INFO)

    steam_handler = logging.FileHandler("my.log", mode="a", encoding="utf8")
    logger.addHandler(steam_handler)

    logging.debug("틀렸잖아!")
    logging.info("확인해")
    logging.warning("조심해!")
    logging.error("에러났어!!!")
    logging.critical("망했다!!!")