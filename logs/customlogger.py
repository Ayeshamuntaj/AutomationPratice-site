import logging
import os
class LogGen:
    @staticmethod
    def loggen():
        path = os.path.abspath(os.curdir) + "/automation.log"  # Corrected path construction
        logging.basicConfig(filename=path, format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)  # Added necessary parameters to basicConfig
        logger = logging.getLogger()  # Corrected method name
        return logger