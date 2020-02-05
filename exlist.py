minha_lista = [1, 2, 3, 4, 5]

# Adicione os numeros 10 e 20 à esta lista
minha_lista.append(10)
minha_lista.append(20)
print( minha_lista)
# Quantos elementos tem esta lista?
print( len(minha_lista) )
# QUal a soma de todos estes elementos?
print( sum(minha_lista) )
# Qual é o ultimo elemento dessa lista?
print( minha_lista[-1] )
# Concatene esta lista com outra [100,122,34]
minha_lista += [100,122,34]
print(minha_lista)
# Qual a média dos valores dessa lista?
media = sum(minha_lista)/len(minha_lista)
print("A média da minha lista é ", media, sep = "")

# Encontre o valor de máximo e o valor de mínimo
print( max(minha_lista) )
print( min(minha_lista) )