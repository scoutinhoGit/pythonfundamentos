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

class Servidor():
    def __init__(self,servico,disco,processador,memoria):
        self.servico=servico
        self.disco=disco
        self.processador=processador
        self.memoria=memoria

    def addMemoria(self,memoria):
        self.memoria+=memoria

    def addDisco(self,disco):
        self.disco+=disco
    
    def changeServico(self,servico):
        self.servico = servico
 
hall9000 = Servidor('psicotico',200,'2000',16) 
print(hall9000.servico,hall9000.memoria,hall9000.disco)
hall9000.addMemoria(15)
hall9000.addDisco(7)
hall9000.changeServico('Hall9000-20b7')
print(hall9000.servico,hall9000.memoria,hall9000.disco)

