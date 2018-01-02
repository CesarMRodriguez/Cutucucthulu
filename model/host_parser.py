import re

class HostParser:

    def parseIpHosts(self,str_ips):
        number0to255 = '(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])'
        number1to35 = '(?:3[0-5]|[12][0-9]|[1-9])'
        number0to255withHyphen =  number0to255 + '(?:-' + number0to255 + ')?'
        commaSeparatedNumber0to255withHyphen = number0to255withHyphen + '(?:,(?:' + number0to255withHyphen + '))*'
        regex = re.compile('^(?P<uno>' + commaSeparatedNumber0to255withHyphen + ')\.(?P<dos>' + commaSeparatedNumber0to255withHyphen + ')\.(?P<tres>' + commaSeparatedNumber0to255withHyphen + ')\.(?P<cuatro>' + commaSeparatedNumber0to255withHyphen + ')(?:\/(?P<mask>' + number1to35 + '))?$')
        if(regex.match(str_ips)):
            result = regex.search(str_ips)
            return [True,result.groups]
        else:
            return [False,[]]