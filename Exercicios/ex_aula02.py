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
    print(i)
# b) Nome dos estados e sua populacao
# c) Nome dos estados e quantidades municipios

#print(dados['estados']['sp']['nome'])
