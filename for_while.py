nome  = "Marina Rodrigues"

minha_lista = [1, 2, 3, ['Mah', 'Rodrigues'], 'Regina']

for i in minha_lista:
    print("Rodando mais uma iteração...")
    print(i)

lista1 = []
for i in range(1, 101):
    lista1.append(i)

lista_100 = range(1,50)

# Começando o while 

contador = 1
while contador <= 10:
    print(contador)
    contador += 1


notas = []
contador = 1
while contador <= 4:
    notas.append(float(input("Aluno dgite sua nota: ")))
    contador += 1