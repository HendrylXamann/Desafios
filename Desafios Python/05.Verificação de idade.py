#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa;
#retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições;

def voto(year):
    from datetime import date #Importação apenas dentro do escopo da função (Essa biblioteca pega a data atual)
    hoje = date.today().year #Uso do método date para atribuir a variável a data de hoje (o ano)
    idade = hoje - year #2023 - ano inserido pelo usuário irá retornar para variável a idade 
    return idade
ano = int(input("Digite o ano em que você nasceu: "))

if voto(ano) >= 18 and voto(ano) < 70:
    print("VOTO OBRIGATÓRIO")
elif voto(ano) >= 16 and voto(ano) <= 17 or voto(ano) >= 70:
    print("VOTO OPCIONAL")
else:
    print("VOTO NEGADO")
