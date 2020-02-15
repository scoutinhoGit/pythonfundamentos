# -*- coding: UTF-8 -*-
# class Automovel():
#     def __init__(self):
#         self.rodas=4
#         self.motor=True

#     def ligar(self):
#         print("ligando o motor")

# palio = Automovel()
# palio.ligar()
# print(palio.rodas)       

# class Servidor():
#     def __init__(self,servico,disco,processador,memoria):
#         self.servico=servico
#         self.disco=disco
#         self.processador=processador
#         self.memoria=memoria

#     def addMemoria(self,memoria):
#         self.memoria+=memoria

#     def addDisco(self,disco):
#         self.disco+=disco
        
#     def changeServico(self,servico):
#         self.servico = servico
 
# hall9000 = Servidor('psicotico',200,'2000',16) 
# print(hall9000.servico,hall9000.memoria,hall9000.disco)
# hall9000.addMemoria(15)
# hall9000.addDisco(7)
# hall9000.changeServico('Hall9000-20b7')
# print(hall9000.servico,hall9000.memoria,hall9000.disco)


# import requests

# class Teste():
#     def __init__(self):
#         self.SITE="https://renatobarbosa.tech"

#     def verificar_site(self):
#         self.requisicao= requests.get(self.SITE)
#         return self.requisicao

#     def verifica_home(self):
#         return self.requisicao.text       


# site01 = Teste()

# print(site01.verificar_site())

#-------
# class Servidor():
#     def __init__(self,servico,disco,processador,memoria):
#         self.servico=servico
#         self.disco=disco
#         self.processador=processador
#         self.memoria=memoria

# class servidorWeb(Servidor):
#     def __init__(self,servico,disco,processador,memoria):
#         # forma de herdar os atributos classe mae
#         super().__init__(servico,disco,processador,memoria)
#         self.servico='Nginx'

# vader=servidorWeb('psicotico',200,'2000',16)
# print(vader.servico,vader.disco)


class Servidor():
    def __init__(self):
        self.disco=10
        self.processador='Rko'
        self.memoria=10

class servidorWeb(Servidor):
    def __init__(self):
        # forma de herdar os atributos classe mae
        super().__init__()
        self.servico='Nginx'

vader=servidorWeb()
print(vader.servico,vader.disco)

