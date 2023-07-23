#Crie uma função que verifica se o número é ímpar ou par:

def imparoupar(numero=0):
    verifica = numero % 2
    if verifica == 0:
        return "Este número é par"
    else:
        return "Este número é ímpar"

a = int(input("Digite um número: "))
print(imparoupar(a))
    
    