class Host:

    def __init__(self):
        self.name = ""
        self.ip = ""
        self.OS = ""
        self.services = []


    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getIP(self):
        return self.ip

    def setIP(self, ip):
        self.ip = ip

    def getOS(self):
        return self.OS

    def setOS(self, os):
        self.OS = os
    
    def getServices(self):
        return self.services

    def setServices(self, services):
        self.services = services
    
    def __str__(self):
        sb = '{"name":"'+self.name+'", \n'
        sb += '"IP":"'+self.ip+'", \n'
        sb += '"OS":"'+self.OS+'", \n'
        sb += '"services":'
        for service in self.services:
            sb += str(service) + ", \n"
        sb += '] }\n'
        
        return sb