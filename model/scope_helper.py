class ScopeHelper:

    def getHosts(str_scope):
        scopeHost = []
        if not len(str_scope) == 0:
            commaSeparatedHosts = splstr_scope.split(',')
            for scopeHost in commaSeparatedHosts:
                if isIP(scopeHost):
                    validateIP

    def isIP(str_host):
        return str_host[0].isDigit():