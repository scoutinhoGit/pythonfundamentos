from unittest import TestCase, main

# aqui forco a tipagem de entrada e saida da funcao
def validar_par(num:int) -> bool:
    if isinstance(num,int):
        return True if num % 2 == 0 else False
    elif isinstance(num,str):
        if num.isnumeric():
            return True if int(num) % 2 ==0 else False



class Testes(TestCase):
    def teste_par(self):
        self.assertEqual(validar_par(4),True)
    def teste_impar(self):
        self.assertEqual(validar_par(1),False)
    def teste_string(self):
        self.assertEqual(validar_par('102'),True)
    def teste_string_null(self):
       self.assertEqual(validar_par('string'),None)


if __name__ == "__main__":
    main()             