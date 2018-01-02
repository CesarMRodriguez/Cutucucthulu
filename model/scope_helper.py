from host_parser import HostParser
class ScopeHelper:

    def getHosts(self, str_scope):
        scopeHosts = []
        resultMsg = ''
        if not len(str_scope) == 0:
            commaSeparatedHosts = str_scope.split(';')
            for host in commaSeparatedHosts:
                error = False
                if self.isIP(host):
                    parser = HostParser()
                    parserResult = parser.parseIpHosts(host)
                    if(parserResult[0]):
                        error = self.addIpHost(scopeHosts,parserResult[1])
                    else:
                        error = True
                
                if(error):
                    resultMsg += 'Invalid host ' + host + '\n'

    def isIP(self, str_host):
        return str_host[0].isDigit()

    def addIpHost(self, hostsList, ipComponents):
        ipNumbers = ipComponents[0:4]
        ipMask
        for component in ipComponents:
