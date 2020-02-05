# O usuário vai chutar um numer entre 1 e 15
# Defina o numero da sorte da sua escolha para ele tentar acertar
# Se o chute dele for muito alto, avise-o com a mensagem: "tente um numero menor"
# Se o chute dele for muito baixo, avise-o com a mensagem: "tente um numero maior"
# Se ele acertar, avise-o com a mensagem: "TU é o bixao memo hein doido"

numero = int(input("Queridissimo usuário digite um número entre 1 e 15, também pode ser o 1 ou o 15: "))

luck_number = 3

if numero == luck_number:
    print("TU é o bixao memo hein doido")

elif numero > 15 or numero < 1:
    print("Querido usuário eu disse um numero ENTRE 1 e 15")

elif numero < luck_number:
    print("Tente um numero maior")

else: 
    print("Tente um numero menor")