# Funcoes
# -*- coding: utf-8 -*-
# produtos=[]

# def f_cadastra_produto(produto):
#     global produtos
#     if len(produto.strip()) > 0:
#         produtos.append(produto)
#         print('insercao OK')
#     else:
#         print('parametro vazio')    
    
# def f_lista_produtos(lista=produtos):
#     print(lista)

# def f_remove_produto(produto):
#     global produtos
#     produtos.remove(produto)
    
# f_cadastra_produto('abacaxi')
# f_cadastra_produto('laranja')
# f_cadastra_produto('pera')
# f_cadastra_produto('banana')
# f_cadastra_produto('abacate')
# f_cadastra_produto('    ')
# f_remove_produto('abacaxi')

#f_lista_produtos()

# crie uma funcao que receba x e y 
# e retorne a soma , subtracao

# def f_soma(x,y):
#     return x+y

# def f_subtracao(x,y):
#     return x-y
    
# valor = f_soma(3,5)   
# print(valor) #

# valor = f_subtracao(3,5)   
# print(valor) 


# Faca uma funcao que receba dos parametros 
# e retorne o maior deles

# def f_maior(x,y):
#     if isinstance(x,int) ==False | isinstance(x,float)==False:
#         print('Nao posso comparar valores nao numericos')
#         return
#     if isinstance(y,int) ==False | isinstance(y,float)==False:
#         print('Nao posso comparar valores nao numericos')
#         return
#     if x > y:
#         print(x)
#         return
#     elif x < y :
#         print(y)
#         return
#     else:
#         print('ambos tem os mesmos valores')
#         return

# f_maior(1,1)      

# f_maior(10.4,1)

# f_maior('A',1.0)

# f_maior(3.123456789012356789012334,3.1234567890)

# ARGS E KARGS
# Args (aqui eu posso inserir qtos parametros quiser)
def maior(*valores):
    print(max(valores))

# maior(1,2,3,4,5,6,7,8,9,0)

# lista=[100,0,2,3,4,5,6]
# print(sorted(lista,reverse=True)[0])

# import requests
# def api(**valores):
#     req=requests.get(valores['url']) 
#     return req

# x=api(url='http://www.xpto.com.br',porta=300,retorno='OK') 
# print(x)   

# funcoes lambada
#var = lambda x: x*3
#print(var(2))
#maior(lambda x: x*3)

#valor = lambda x,y: x-y
#print(valor(4,3))

itens=[1,2,3,4,5]

#double = list(map(lambda x: x*2,itens))
#print(double)
#tripĺo=map(lambda x: x*2,itens)
#print(tripĺo)

from functools import reduce
itens=[1,2,3,4,5,6,7,8,9,0,12121.1212,1,11111212121212121212121444555556666662,2,2,3,4,5,5,6,222222222222222]
# exemplo de filtragem
lista_filtrada_par = list(filter(lambda x: x %2 == 0,itens))
# exemplo de reduce
soma = reduce((lambda x,y: x+y),lista_filtrada_par)

print(soma)
