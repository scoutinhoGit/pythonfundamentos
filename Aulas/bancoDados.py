# POSTGREE
# 
# import psycopg2

# try:
#     print("Abrindo conexao banco")
#     con = psycopg2.connect("host=localhost dbname=projeto user=admin password=4linux")
    
#     print("Iniciando Cursor")  
#     cur = con.cursor()

#     print("Efetuando insert")
#     cur.execute("insert into scripts (nome,conteudo) values ('xpto','lingua plesa,gato manco')")

#     print("Comitando inclusao")
#     con.commit() 

# except Exception as e:
#     print(f'Erro: {e}')
#     print("Fazendo rollback")
#     con.rollback()

# finally:
#     print("Encerrando cursor banco")
#     con.close()
#     print("Encerrando conexao banco")
#     con.close()

# MONGODB
from pymongo import MongoClient

client =MongoClient('localhost')
db = client['dexterops']

def inserir_dados():
    try:
        db.fila.insert({"_id":3,"empresa":"4linux","cursos":[{"nome":"Python II","Carga Horaria":10},{"nome":"Linux III","Carga Horaria":5}]})
    except Exception as e:
        print(f"Erro: {e}")

#inserir_dados()    

def buscar_dados():
    for r in db.fila.find():
        print('Empresa {}'.format(r['empresa'])) 
        for c in r['cursos']:
            print(20*'=')
            print('Nome : {} \n Carga Horaria {}'.format(c['nome'],c['Carga Horaria']))    

buscar_dados()                 