import configparser

config = configparser.RawConfigParser()

config.read("C:\\Users\\DELL\\PycharmProjects\\Orangehrm_Demo_1\\Configuration\\config.ini")

class ReadValue():

    @staticmethod
    def getUsername():
        username = config.get('Login info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('Login info', 'password')
        return password

    @staticmethod
    def getUrl():
        url = config.get('Login info', 'Url')
        return url

