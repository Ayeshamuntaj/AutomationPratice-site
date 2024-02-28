import configparser
import os.path

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.path.join(os.curdir,"configuration" ,"config.ini")))
class ReadConfig:
    @staticmethod
    def getApplicationurl():
        url=config.get("commonInfo","baseurl")
        return url