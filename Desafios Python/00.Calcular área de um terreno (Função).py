#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre
#a área do terreno:

def area(largura,comprimento):
    resultado = largura * comprimento
    return resultado

a = float(input("Digite a Largura do terreno:"))
b = float(input("Digite o Comprimento do terreno:"))
print(f"A área do terreno de {a}x{b} é de",area(a,b),"m²")
