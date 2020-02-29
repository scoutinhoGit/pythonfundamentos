from sqlalchemy import update
from core import user_table,  engine

con = engine.connect()
#upd = user_table.update()

def atualizar_dados(antigo_nome,novo_nome):
    ''' Funcao atualiza dados:
           n = nome
    '''
    upd = update(user_table).where(user_table.c.nome==antigo_nome)
    upd = upd.values(nome=novo_nome)
    result = con.execute(upd)
    print(result.rowcount)

atualizar_dados('Xpto4','Xpto5')   
      
