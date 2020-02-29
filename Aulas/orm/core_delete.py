from sqlalchemy import delete
from core import user_table,  engine

con = engine.connect()
#upd = user_table.update()

def delenda_datus(dado):
    ''' Funcao delete dados :
           n = nome
    '''
    dele = delete(user_table).where(user_table.c.nome==dado)
    result = con.execute(dele)
    print(result.rowcount)

delenda_datus('Xuxu')   
      
