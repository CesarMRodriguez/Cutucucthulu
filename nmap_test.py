from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException
from model.host import Host
from model.service import Service
import pprint

def addOS(host, nmap_host):
    #Resolver en caso de que no sea 100% cierto, qué puede llegar a ser en base a 
    #los servicios o sino tratar de truncar el servicio
    if (nmap_host.os_fingerprinted):
        host.setOS(nmap_host.os_fingerprint)

def print_report(nmap_report):
    hosts = []
    for host in nmap_report.hosts:
        host_object = Host()
        if len(host.hostnames):
            tmp_host = host.hostnames.pop()
        else:
            tmp_host = host.address

        host_object.setName(tmp_host)
        host_object.setIP(host.address)
        addOS(host_object, host)
        print("Nmap scan report for {0} ({1})".format(
            tmp_host,
            host.address))
        print("Host is {0}.".format(host.status))
        print("  PORT     STATE         SERVICE")

        services = []
        for serv in host.services:
            service = Service()
            pserv = "{0:>5s}/{1:3s}  {2:12s}  {3}".format(
                    str(serv.port),
                    serv.protocol,
                    serv.state,
                    serv.service)
            service.setName(serv.service)
            service.setPort(str(serv.port))
            service.setState(serv.state)
            service.setType(serv.protocol)
            #Agregar alguna forma de separar el nombre de la versión del número de la misma
            if len(serv.banner):
                service.setDescription(serv.banner)
                pserv += " ({0})".format(serv.banner)
            print(pserv)
            services.append(service)
        host_object.setServices(services)
    
    hosts.append(host_object)
    print(nmap_report.summary)
    return hosts

print "Antes de procesar"
nm = NmapProcess("localhost", options="-A")
rc = nm.run()
print "Despues de procesar"

if nm.rc == 0:
    try:
        parsed = NmapParser.parse(nm.stdout)
        res = print_report(parsed)
        for host in res:
            print host
    except NmapParserException as e:
        print("Exception raised while parsing scan: {0}".format(e.msg))

else:
    print nm.stderr