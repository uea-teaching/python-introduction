"""logging module example"""
import logging
from log_aux import some_function

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

logging.info("calling from main: root logger")
some_function()
