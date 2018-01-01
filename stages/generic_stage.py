import sys
import globals

class GenericStage:

    def getOptions(self):
        return self.options


    def getMainOption(self):
        return self.mainOption


    def __init__(self):
        self.prompt = "reconmaster>"
        self.options = []
        self.mainOption = "generic"

    def fillOption(self,option):
        self.options.append(option)

    def getPrompt(self):
        return self.prompt

    def executeStage(self):
        while True:
            value = raw_input(self.getPrompt())
            if value == '-h' or value == 'help':
                self.printHelp()
            elif value == 'back':
                break
            elif value == 'exit':
                self.close()
                sys.exit()
            else:
                self.executeOptions(value)

    def close(self):
        globals.db.close()

    def printGeneralOptions(self):
        print 'General options applicable to this stage:'
        print '\t-h or help:    shows help options'
        print '\tback:          goes to the previous menu'
        print '\texit:          closes the program'
        print ''
        
    def printHelp(self):
        self.printGeneralOptions()
        print 'Available stages:'
        for option in self.getOptions():
            print '\t' + option.getDescription()

    def executeOptions(self, value):
        optionFound = False
        for option in self.options:
            if option.getMainOption() == value:
                option.executeStage()
                optionFound = True
                break
        
        if not optionFound:
            print 'The function "' + value + '" does not exist.'