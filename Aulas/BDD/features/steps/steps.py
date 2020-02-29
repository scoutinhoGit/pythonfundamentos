from behave import step

def soma(x:int,y:int)-> int:
    return x+y

@step('somar "{num1}" com "{num2}"')
def teste_soma(context,num1,num2):
    context.r_soma = soma(int(num1),int(num2))    

@step('o resultado deve ser "{esperado}"')
def teste_soma_result(context,esperado):
    assert context.r_soma == int(esperado), "teste falhou"
