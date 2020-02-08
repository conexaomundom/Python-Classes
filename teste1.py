# Crie um programa que leia um inteiro.
# A seguir, calculeo menor número de notas possíveis (cédulas)
# no qual o valor pode ser decomposto
# As notas consideradas são de 100, 50, 20, 10, 5, 2, 1
# A seguir mostre o valor lido e a relação de notas necessarias.

possiveis_notas = [ 100, 50, 20, 10, 5, 2, 1]
# dicionario_notas = {"Notas de 100", "Notas de 50", "Notas de 20", "Notas de 10", "Notas de 5", "Notas de 2", "Notas de 1"}
# valor = int( input("Digite o valor desejado: "))
valor = 555

quantas = []
for i in range(1, len(possiveis_notas)):
    quantas.append(int(valor/possiveis_notas[i-1]))

dicionario_notas = {"Notas de 100" : quantas[0], "Notas de 50" : quantas[1], "Notas de 20" : quantas[2], "Notas de 10": quantas[3],"Notas de 5": quantas[4], "Notas de 2": quantas[5], "Notas de 1": quantas[6]}

print(dicionario_notas)
