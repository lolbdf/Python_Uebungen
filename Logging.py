import logging

logging.basicConfig(filename="log.log", level=logging.INFO)

logger = logging.getLogger("meinLogger")

logger.setLevel(logging.DEBUG)

fileh = logging.FileHandler("logme.log")

form = logging.Formatter("%(name)s - %(levelname)s : %(asctime)s - %(message)s")

fileh.setFormatter(form)

logger.addHandler(fileh)

logging.info("dies ist eine Info")

logger.debug("debugging")


