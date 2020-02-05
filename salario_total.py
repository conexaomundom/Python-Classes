# Criar um programa que calule o salario do funcionario
# Ele informará quantas horas trabalhou e o valor por horas
# Exiba o montante total

hora = float(input("DIgigte o total de horas trabalhadas: "))
valor_horas = float(input("Digite quanto custa o valor da hora de trabalho: R$ "))

salario = hora * valor_horas

print("Seu salário será: R$:", salario, sep = "")
