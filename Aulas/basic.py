#! /usr/bin/python3
'''
#print saida de dados
print("Python")

# Bool
True
False

#Float
10.5
1.343434

# String
"100"
"jose da silva"

nome="jose"
print(nome)

usuario=input("Digite seu nome: ")
print(usuario)

n1=int(input("digite 1 numero "))
n2=int(input("digite 2 numero "))
print(n1+n2)


#faca 1 programa que receba 4 notas de aluno, some e divide por 4
n1=float(input("Entre com nota 01 "))
n2=float(input("Entre com nota 02 "))
n3=float(input("Entre com nota 03 "))
n4=float(input("Entre com nota 04 "))
media=(n1+n2+n3+n4)/4
print("Media ",media)

print("as notas foram {},{},{},{}".format(n1,n2,n3,n4))
print(f"as notas foram {n1},{n3},{n2},{n4}")

palavra='zpdsd sdsd sdsd ewrwew a'
print(palavra.split())
palavra.upper()
'''

lista = ['Corinthians', [1, 2, 3, 4, 5] ,'Palmeiras', 'Sao Paulo', [10, 11, 12, 13, 14],'Flamengo', 'Vasco']


# print 3, 13, vasco
print(lista[1][2],lista[4][3],lista[5])
#print 4, Sao Paulo, 14
print(lista[1][3],lista[3],lista[4][4])
# print Corinthians, 2, 10, 14
print(lista[0],lista[1][1],lista[4][0],lista[4][4])

print(lista.index('Palmeiras'))
lista.append('Bragantino')
print(lista)
lista.pop()
print(lista)
lista.insert(0,'Sport')
print(lista)
lista.remove('Sport')
print(lista)