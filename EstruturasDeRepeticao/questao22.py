
# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

n = int(input("Digite um número inteiro: "))
lista = []
contador = 0

for i in range(1, n+1):
  if n % i == 0:
    contador += 1

if contador == 2:
  print("Número primo!")
else:
  for i in range(1, n+1):
    if n % i == 0:
      lista.append(i)

if contador > 2:
  print(f"O número {n} é divisível por", end=": ")
  print(lista)

    