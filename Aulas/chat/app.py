import from modules.banco as banco
import threading 

if __name__ == "__main__":
    user = input ("Nickname: ")
    try:
        f = threading.Thread(target=banco.select)
        f.start()
    except Exception as e:
        print("Falha ao criar thread: {}".format(e))
    while f.is_alive:
        mens = input()
        
