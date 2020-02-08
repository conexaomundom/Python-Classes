# Leia 3 valores, no caso as variaveis A, B e C, que são as 
# tres notas de um aluno. A seguir, calcule a média do aluno,
# sabendo que a nota A tem peso 0.2, a nota B tem peso 0.3 e a nota 
# C tem peso 0.5. Considere que cada nota pode ir de 0 a 10, sempre
# com uma casa decimal.

notas = []
pesos = [ .2, .3, .5]
ponderando = []
i = 0
while i <= 2 :
    notas.append( float( input( "Aluno, digite sua nota: ") ) )
    ponderando.append( notas[i] * pesos[i])
    i += 1

print("Queridissimo aluno, a sua media foi: ", sum(ponderando), sep = "")

# Calcule o consumo medio de um automovel sendo fornecido
# a distancia total em km e o total de combustivel gasto em litros


distancia = float( input( "Digite a distância total percorrida em Km: "))
gasto_combustivel = float( input( "Digite o gasto total de combustivel em litros: "))

print("O consumo médio de combustivel do seu automovel foi: ", distancia/gasto_combustivel, " litros por Kl", sep = "")

# Crie um algoritmo para ler um valor em RS(reais)
# e ler a cotação em dolar e fazer a conversão

reais = float( input( "Digite quantos reais vc tem querido usuario: R$ "))
cotacao_dolar = float( input( "Digite quanto esta acotacao dolar hoje querido usuario: U$ "))

print("Querido usuario vc tem: U$ ", reais / cotacao_dolar, " para gastar nos states.", sep = "")




# Crie um programa que receba um numero natural de 1 a 12 e 
# retorne o mês correspondente.

meses = [ "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

mes = int( input( "Digite o numero do mes que vc quer saber: "))

print("O mês que vc está falando é: ", meses[mes-1], sep = "")
 






 # Crie um programa que leia dois valores inteiros e armzene-os nas variáveris A e B
# Efetue a soma de  A e B atribuindo o seu resultado na variavel
# X. Imprima X.

A = int( input( "Querido usuário digite um número inteiro: ") )
B = int( input( "Querido usuário digite outro número inteiro: ") )

X = A + B

print("A soma dos dois valore que vc digitou é: ", X)






# A formula para calcular a area de uma circunferencia
# é area = pi * raio ** 2, considerando nesse problema que 
# pi = 3.14159. Efetue o calculo da area , elevando o valor 
# de raio ao quadrado multiplicado por pi, imprima o resultado.

pi = 3.14159

# raio, vou perguntar ao usuario
raio = float( input( "Querido usuário digite o valor do raio da circunferencia que deseja calcular a área: " ) )

print("Querido usuário, a área da circunferencia que vc queria calcular é: ", (raio ** 2) * pi, sep = "")

# Faça um programa que leia o nome do vendedor,
# o seu salario fixo e o total de vendas efetuadas por ele no mÊs (em dinheiro)
# Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
# informar o total a receber no final do mÊs com duas casas decimais.

nome_vendedor = input("Querido Vendedor escreva o seu nome por favor: ")
salario_fixo = float( input("Querido Vendedor escreva o seu salario fixo por favor: R$ ") )
vendas_efetuadas = float( input("Querido Vendedor digite o valor em vendas efetuadas por favor: R$ ") )

salario_final = salario_fixo + (vendas_efetuadas * .15)
dic_vendedor = {"Nome do Vendedor" : nome_vendedor, "Salario Fixo" : salario_fixo, "Valor em vendas efetuadas" : vendas_efetuadas, "Salario final" : salario_final}


# Crie um programa que leia um inteiro.
# A seguir, calculeo menor número de notas possíveis (cédulas)
# no qual o valor pode ser decomposto
# As notas consideradas são de 100, 50, 20, 10, 5, 2, 1
# A seguir mostre o valor lido e a relação de notas necessarias.

possiveis_notas = [ 100, 50, 20, 10, 5, 2, 1]
dicionario_notas = {"Notas de 100", "Notas de 50", "Notas de 20", "Notas de 10", "Notas de 5", "Notas de 2", "Notas de 1"}

valor = int( input("Digite o valor desejado: "))

quantas = []
for i in range(1, len(possiveis_notas)):
    quantas.append(int(valor / possiveis_notas[i-1]))

dicionario_notas{"Notas de 100" : quantas[0], "Notas de 50" : quantas[1],
                 "Notas de 20" : quantas[2], "Notas de 10": quantas[3],
                 "Notas de 5": quantas[4], "Notas de 2": quantas[5],
                  "Notas de 1": quantas[6]}

print(dicionario_notas)