#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmentro e mostre uma mensagem com tamanho adaptável.

def escreva(texto):
    linhas = len(texto)
    print('-' * linhas)
    print(texto)
    print('-' * linhas)
dado = input("Digite alguma coisa:")
escreva(dado)

