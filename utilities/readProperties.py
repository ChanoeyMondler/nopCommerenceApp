import configparser

# read data from config.ini file
config = configparser.RawConfigParser()
config.read(".\\Configrations\\config.ini")


class ReadConfig:
    @staticmethod
    def getapplicationurl():
        url = config.get("common info", "baseURL")
        return url

    @staticmethod
    def getusername():
        username = config.get("common info", "username")
        return username


    @staticmethod
    def getpassword():
        password = config.get("common info", "password")
        return password
