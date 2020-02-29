from core import user_table,engine

con = engine.connect()
ins = user_table.insert()

def insere_dados(i,n,s):
    ''' Funcao insere dados:
           i = idade
           n = nome
           s = senha
    '''
    new = ins.values(idade=i,nome=n,senha=s)
    con.execute(new)

insere_dados(5,'Xule','xpto4')   
      
