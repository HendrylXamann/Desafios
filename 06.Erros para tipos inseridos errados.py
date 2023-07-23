#Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do python, só que;
#Fazendo a validação para aceitar apenas um valor numérico.

def LeiaInt(dados):
    #Essas são apenas duas variáveis declaradas que serão utilizadas dentro do enquanto:
    booleano = False 
    valor = 0
    while True: #Cria um loop
        numero = str(input(dados)) #A variável número vai receber um dado que será convertido em string;
        if numero.isnumeric(): #Vai verificar se o texto é 100% númerico, caso seja:
            valor = int(numero) #vai converter para inteiro 
            booleano = True #Transformar a variável em verdadeira e nas linhas seguintes fará com que o loop termine
        else:
            print("ERROR! Please querido(a), digite um número INTEIRO válido") #Caso o valor inserido não seja um inteiro vai aparecer essa mensagem
        if booleano: #Se essa variável for true então o loop para!
            break       
    return valor #Vai retornar o dado inserido pelo usuário, já verificado;
numero = LeiaInt('Digite um número inteiro positivo:') 
print(f'Você digitou {numero}')   