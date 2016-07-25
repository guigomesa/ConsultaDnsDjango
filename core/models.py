from django.db import models
from core import Helpers



# Create your models here.

class ConsultaDominio():
    def __init__(self, dominio):
        self.Dominio = dominio
        self.EmailMx = []
        self.EmailDns = []
        self.NameServers = []
        self.Consultar()
        self.SiteEstaOnline = Helpers.HostEstaOnline(self.Dominio)
        pass

    def Consultar(self):
        self.EmailMx = Helpers.GetInfoHost(self.Dominio, Helpers.TipoConsulta.Mx)
        self.NameServers = Helpers.GetInfoHost(self.Dominio, Helpers.TipoConsulta.Ns)

        for x in Helpers.GetInfoHost('mail.'+self.Dominio,Helpers.TipoConsulta.Cname):
            self.EmailDns.append(x)

        for x in Helpers.GetInfoHost('webmail.' + self.Dominio, Helpers.TipoConsulta.Cname):
            self.EmailDns.append(x)
        pass


class ItemDominio():
    def __init__(self):
        self.Host = ""
        self.Ip = ""
        self.EstaOnline = False