"""logging handler example."""

import logging

filehandler = logging.FileHandler("debug.log")
filehandler.setLevel(logging.DEBUG)

streamhandler = logging.StreamHandler()
streamhandler.setLevel(logging.INFO)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[filehandler, streamhandler]
)
logging.debug("This will go to the debug log file")
logging.info("See the debug log file and std err.")
logging.warning("And this, too")
