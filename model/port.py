#Por ahora no se usa
class Port:

    def __init__(self):
        self.port_number = 0
        self.description = ""
        self.state = ""

    def getPortNumber(self):
        return self.port_number

    def setPortNumber(self, port_number):
        self.port_number = port_number

    def getDescription(self):
        return self.description

    def setDescription(self,description):
        self.description = description

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state