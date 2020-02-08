# Laco repeticao for

# frutas = ['abacaxi','banana','caju']
# for i in frutas:
#     if i == 'banana':
#         pass
#     else:
#         print(i)        

#carros = ('astra','belina','camaro')
#for auto in carros:
#    print(auto)

# itens=[]
# for item in range(1,100):
#     itens.append(item)

# print(itens)

# for i in (1,2,3,47):
#     print(i)

# for i in range(1,100,3):
#      print(i)

# carros=['astra','fusca','dkw']
# cores = ['branco','verde','marrom']
# for auto in carros:
#     for paleta in cores:
#         print (f'{auto} {paleta}')

# Erro e excessoes

# try:
#     if nome == 'renato':
#         print(nome)
# except Exception as erro:
#     print(f'Erro: {erro}')      

# while True:
#     try:
#         x = int(input('Digite 1o numero: '))
#         y = int(input('Digite 2o numero: '))
#         print(x+y)
#         break
#     except ValueError:
#         print('digite apenas numeros!')
#     finally:  # passa aqui mesmo quando ocorre erro
#          print('ufa')   

# blaclkist =['xuao','belo']
# try:
#     nome = input('Digite nome ')
#     print(nome)
#     if nome in blacklist:
#         raise Exception ex_ErroNome('Usuario bloqueado')
# except ex_ErroNome as n:
#     print(n)

# usuarios = ['Caio','Filipe','Manuela','Daniel','Camila']

# while True:
   
#     try:
#         nome = input('Informe usuario : ')
#         if nome in usuarios:
#            print('Acesso Liberado')
#            break
#         else:
#            raise NameError ('Perigo Perigo. Digite novamente ')
#            continue
#     except NameError as e:
#         print (e) 


# # you need to guess this number
# number = 10
# while True:
#    try:
#        i_num = int(input("Enter a number: "))
#        if i_num < number:
#            raise ValueTooSmallError
#        elif i_num > number:
#            raise ValueTooLargeError
#        break
#    except ValueTooSmallError:
#        print("This value is too small, try again!")
#        print()      
# 

# Manipulacao de arquivos

# with open('arquivo.txt','w') as arq:
#     arq.writelines('xpto')
#     arq.writelines('xpto')
#     arq.writelines('xpto')
#     arq.writelines('xpto')
#     arq.writelines('xpto')
#     arq.writelines('xpto')
#     arq.writelines('xpto')
#     arq.writelines('xpto')
#     arq.close()

# with open('arquivo.txt','a+') as arq:
#     arq.seek(0)
#     arq.writelines('xpto2 inicial deo arquisocairawidhasjkdasdjasd')
#     arq.close()

#!/usr/bin/python

# Open a file
# fo = open("foo.txt", "r+")
# print("Name of the file: ", fo.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

# line = fo.readline()
# print ("Read Line: %s" % (line))

# # Again set the pointer to the beginning
# fo.seek(2,0)
# line = fo.readline()
# print ("Read Line: %s" % (line))

# # Close opend file
# fo.close()


# with open('arquivo.txt','w') as arq:
#     for i in range(1,100):
#         arq.write('xpto\n')
#     arq.close()    

# 