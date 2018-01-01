from generic_stage import GenericStage
from database_management import DatabaseConnection
import globals

class ScopeDB(GenericStage):

    def __init__(self):
        self.prompt = "reconmaster/scope>"
        self.mainOption = "scope"

    def getDescription(self):
        return 'scope: management of scope in the workspace selected'

    def printHelp(self):
        self.printGeneralOptions()
        
        print 'Options for Scope Stage: '
        print '\tadd:       adds a new host to the workspace'
        print '\tdelete:    deletes a host in the workspace'
        print '\tshow:      show the hosts in the workspace'
        print '\texclude:   excludes a host of being processed by the tools'
        print '\tinclude:   includes a host to be processed by the tools'
        print ''
        print 'options of hosts to include'
        print '---------------------------'
        print '- url: url without port, scheme, path or parameters --> www.google.com.ar '
        print '- ip: IPv4 without port --> 127.0.0.1'
        print '- ip range: range of IPs with subnet mask --> 192.168.1.1/24'
        print '- ip range: range of IPs with start and end octet part --> 192.168.1-10.1-125'
        print '- ip list: list of ips separated with commas --> 192.168.1.1,192.168.1.10'

    def executeOptions(self, value):
        optionFound = False
        if value == 'add':
            self.addHost()
            optionFound = True
        elif value == 'delete':  
            self.deleteHost()
            optionFound = True
        elif value == 'show':
            self.showHost()
            optionFound = True
        elif value == 'exclude':
            self.excludeHost()
            optionFound = True
        elif value == 'include':
            self.includeHost()
            optionFound = True
        
        if not optionFound:
            print 'The function "' + value + '" does not exist.'
        
    def addHost(self):
        host = raw_input(self.prompt+ 'Host to add:')
        
        
        
