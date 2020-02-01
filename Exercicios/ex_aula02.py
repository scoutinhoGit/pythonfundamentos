# -*- coding: utf-8 -*-

dados={'estados':{
                   'sp':{'nome':'Sao Paulo',
                         'municipios':645,
                        'populacao':44.04},
                   'rj':{'nome':'Rio Janeiro',
                         'municipios':92,
                         'populacao':16.72},
                   'mg':{'nome':'Minas Gerais',
                         'municipios':31,
                         'populacao':20.8}                                   
                }
       }

# print(dados)      

# imprima as informacoes
# a) Nome dos Estados
for i in dados['estados'].keys():
    print(f"Nome do estado [{i}] : {dados['estados'][i]['nome']}")
 
 # b) Nome dos estados e sua populacao
for i in dados['estados'].keys():
    print(f"Nome do estado [{i}] : {dados['estados'][i]['nome']} tem populacao de {dados['estados'][i]['populacao']}")
# c) Nome dos estados e quantidades municipios
for i in dados['estados'].keys():
    print(f"Nome do estado [{i}] : {dados['estados'][i]['nome']} tem {dados['estados'][i]['municipios']} municipios")
#print(dados['estados']['sp']['nome'])
