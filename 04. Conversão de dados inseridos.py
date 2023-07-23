#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome do jogador e quantas cestas ele fez;
#O Programa tem que mostrar a ficha do jogador, mesmo que o usuário tenha inserido alguma informação incorreta;

#Resultado:
def fichajogador(atleta="****", pontos=0):
    print(f"O jogador {atleta} fez {pontos} pontos até o momento")
  
nome = str(input("Digite o nome do jogador: "))
cestas = str(input("Digite quantas cestas ele fez: "))

if cestas.isnumeric(): #Condicional utilizando método isnumeric para verificar se o texto é 100% númerico
    cestas = int(cestas) #Caso seja, o valor inserido vai ser convertido em int
else:
    cestas = 0 #Caso contrário irá inserir o 0

if nome.strip() == '': #Condicional usando método strip para elimininar todos os espaços e verificar se o nome está vazio;
    fichajogador(pontos=cestas) #Se o usuário passar o nome do jogador como vazio, então vai aparecer só a qtd de cestas;
else:
    fichajogador(nome, cestas) #Se o o usuário inserir os 2, vai aparecer os 2;

#Obs: Claro que para esta última condicional, se o usuário não inserir nada em nome o valor pré definido **** irá aparecer.





