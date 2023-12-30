# -*- coding: utf-8 -*-
# !/usr/bin/python3

import os
import time
import traceback
import logging
import urllib.request

from Misc import get911, sendEmail


def check_internet():
    """
    Check internet connectivity by attempting to retrieve the external IP address.

    Returns:
        bool: True if internet is available, False otherwise.
    """
    for _ in range(3):
        try:
            logger.info("Getting external IP...")
            urllib.request.urlopen("https://v4.ident.me/").read().decode("utf8")
            return True
        except Exception as ex:
            logger.error("Failed to get external IP")
            logger.error(ex)
            time.sleep(5)

    return False


def main():
    """
    Main function to check internet connectivity and reboot the system if it is not available.
    """
    # Reset Internet Interface if NO internet
    if check_internet():
        logger.info("Internet is available.")
    else:
        logger.info("Internet is not available. Rebooting...")
        os.system("sudo reboot")

    return


if __name__ == '__main__':
    # Set Logging
    LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.abspath(__file__).replace(".py", ".log"))
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()])
    logger = logging.getLogger()

    logger.info("----------------------------------------------------")

    try:
        main()
    except Exception as ex:
        logger.error(traceback.format_exc())
        sendEmail(os.path.basename(__file__), str(traceback.format_exc()))
    finally:
        logger.info("End")
