from pymongo import MongoClient, DESCENDING
import time


class BancoMongo():
    def __init__(self):
        try:
            client = MongoClient('192.168.200.111')
            self.db = client['chat']
        except Exception as e:
            print(e)
            exit

    def cadastrar(self, p_nome, p_mensagem):
        date = {'nome': p_nome, 
                'mensagem': p_mensagem,
                'hora': time.strftime('%d-%m-%Y %H:%M:%S')}
        self.db.chat.insert(date)        

    def visualizar(self):
        ultimo_registro = [rg for rg in self.db.chat.find().sort("_id",DESCENDING)]
        while True:
             date = [rg for rg in self.db.chat.find().sort("_id",DESCENDING)]
             if date != ultimo_registro:
                 ultimo_registro = date
                 dado = ultimo_registro[0]
                 print("[{}] {} : {} \n".format (dado['hora'],dado['nome'],dado['mensagem']))
             time.sleep(2)
            