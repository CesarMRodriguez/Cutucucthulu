class Service:

    def __init__(self):
        self.name = ""
        self.port = ""
        self.description = ""
        self.type = ""
        self.version = ""
        self.state = ""

    def getState(self):
        return self.state

    def setState(self,state):
        self.state = state

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getPort(self):
        return self.port

    def setPort(self, port):
        self.port = port

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getVersion(self):
        return self.version

    def setVersion(self, version):
        self.version = version

    def __str__(self):
        sb = '{"name":"'+self.name+'", \n'
        sb += '"port":"'+self.port+'", \n'
        sb += '"description":"'+self.description+'", \n'
        sb += '"type":"'+self.type+'", \n'
        sb += '"version":"'+self.version+'", \n'
        sb += '"state":"'+self.state+'"}\n'
        return sb