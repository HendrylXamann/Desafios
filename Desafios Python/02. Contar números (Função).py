#Faça um programa que tenha uma função chamada CONTADOR(), que receba três parâmetros: início, fim e passo e realiza a contagem.
#o programa tem que realizar três contagens atráves da função criada: A) De 1 até 10, de 1 em 1; B) De 10 até 0, de 2 em 2; C)Uma contagem personalizada;


#A) De 1 até 10, de 1 em 1;
def contadorA(comeco,fim,passo):
    print("Contar de",comeco, "até",fim,"de",passo,"em",passo) #Forma alternativa seria: print(f'Contar de{comeco} até {fim} de {passo} em {passo}')
    conta = comeco #Delimitando o valor inicial (que vai ser inserido quando a função for evocada)
    while conta <= fim: #um laço que basicamente está condicionando a realização, enquanto conta (1) for menor ou igual fim(10) ele vai incrementar o passo(1)
        print(conta)#até chegar no fim e printar isso;
        conta += passo   
    print("\n")            
contadorA(1,10,1)

#O resultado é exprimido em 10 linhas de forma vertical, para fazer sair todos os números em uma mesma linha é só por um end='' no print(conta)

#B) De 10 até 0, de 2 em 2; Eu poderia fazer todas as alternativas em uma única função, mas vou fazer fragmentado para melhor elucidar a consulta/estudos posterior
def contadorB(comeco,fim,passo):
    print(f'Contar de {comeco} até {fim} de {passo} em {passo}')

    if comeco < fim: #Se o valor do primeiro parâmetro for menor que o segundo (começo menor que fim) ele faz:
        conta = comeco #Delimita o valor inicial (que vai ser inserido quando a função for evocada)
        while conta <= fim: #um laço que basicamente está condicionando a realização, enquanto conta (1) for menor ou igual fim(10) ele vai incrementar o passo(1)
            print(conta)#até chegar no fim e printar isso;
            conta += passo
        print("\n")    
    else: #mas se não atender a condional if:
        conta = comeco #Delimita o valor inicial (que vai ser inserido quando a função for evocada)
        while conta >= fim: #Enquanto conta for maior ou igual, no caso enquanto 10 for maior ou igual 0 ele vai:
            print(conta," ", end='') 
            conta -= passo  #Pegar o valor inicial, 10, e ir retirando o valor do passo que é 2 ---- Basicamente o inverso da função A 
        print("\n")       
contadorB(10,0,2)


#C)Uma contagem personalizada;
def contadorC(comeco,fim,passo):
    print(f'Contar de {comeco} até {fim} de {passo} em {passo}')

    if comeco < fim: 
        conta = comeco 
        while conta <= fim: 
            print(conta," ", end='') 
            conta += passo 
        print("\n")

    else: #
        conta = comeco 
        while conta >= fim: 
            print(conta," ", end='') 
            conta -= passo   
        print("\n")      
a = int(input("Digite o valor inicial: "))
b = int(input("Digite o valor final: "))
c = int(input("Digite o valor de pulo: "))
contadorC(a,b,c)
