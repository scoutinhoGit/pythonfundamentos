from unittest import TestCase,main

def somar(x,y):
    return x+y

def dividir(x,y):
    return x/y

def subtrair(x,y):
    return x-y   
    
def multiplicar(x,y):
    return x*y    

#assert somar(2,2)==4 ,"Obtido {}, Esperado: 4".format(somar(2,2))      

class Testes(TestCase):
    def teste_soma(self):
        self.assertEqual(somar(5,5),10)
        self.assertLess(somar(5,5),11)
    
    def teste_sub(self):
        self.assertEqual(subtrair(5,5),0)
        self.assertLessEqual(subtrair(5,5),11)  

    def teste_div(self):
        self.assertEqual(dividir(5,5),1)
        self.assertLessEqual(dividir(5,5),0)     

# So executa se chamado este script .. sem importar a partir de outro
if __name__ == "__main__":
    main()  # este eh o da biblioteca
          
