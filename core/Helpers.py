import socket
import dns.resolver
import os
from enum import Enum
from . import models

class TipoConsulta(Enum):
    Mx = 'MX'
    Ns = 'NS'
    Cname = 'CNAME'



def HostEstaOnline(host):
    try:
        isAlive = os.system("ping -c 1 " + host)
        return isAlive == 0
    except Exception:
        return False


def GetInfoHost(host, tipoConsulta):
    retorno = []
    try:
        if(tipoConsulta == TipoConsulta.Mx):
            temporario = dns.resolver.query(host, TipoConsulta.Mx.name)
        elif(tipoConsulta == tipoConsulta.Ns):
            temporario = dns.resolver.query(host, TipoConsulta.Ns.name)
        elif(tipoConsulta == TipoConsulta.Cname):
            temporario = dns.resolver.query(host, TipoConsulta.Cname.name)
        else:
            return retorno

        for x in temporario:
            try:
                temp = models.ItemDominio()
                temp.Host = x.to_text()
                temp.Ip = socket.gethostbyname(temp.Host)
                temp.EstaOnline = HostEstaOnline(temp.Host)
                retorno.append(temp)
            except Exception:
                continue
    except Exception:
        b = ""
    return retorno

