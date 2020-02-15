import psycopg2

try:
    print("Abrindo conexao banco")
    con = psycopg2.connect("host=localhost dbname=projeto user=admin password=4linux")
    
    cur = con.cursor()

    print("Efetuando insert")
    cur.execute("insert into scripts (nome,conteudo) values ('xpto','lingua plesa,gato manco')")

    print("Comitando inclusao")
    con.commit() 

except Exception as e:
    print(f'Erro: {e}')
    print("Fazendo rollback")
    con.rollback()

finally:
    print("Encerrando conexao banco")
    con.close()