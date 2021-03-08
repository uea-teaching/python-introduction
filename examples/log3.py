"""Setting logging formatted example"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug("This message will not go to the log file")
logging.info("This will go to the log file.")
logging.warning("And this, too")
logging.error("That's torn it!!")
