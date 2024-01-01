import logging


#class LogGen:
 #   @staticmethod
 #   def loggen():
  #      logging.basicConfig(filename=r"C:\Automation_scripts\nopcommerceApp\Logs\logssss.py",
   #                         format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    #    logger = logging.getLogger()
     #   logger.setLevel(logging.INFO)
      #  return logger


import logging

class LogGen:
    @staticmethod
    def loggen():
        # Creating logger
        logger = logging.getLogger(__name__)

        # Creating file handler and setting the formatter
        fileHandler = logging.FileHandler(filename=r"E:\AUtomation_projects\Logs\automation.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        # Adding file handler to the logger
        logger.addHandler(fileHandler)

        # Setting the logging level
        logger.setLevel(logging.DEBUG)

        return logger