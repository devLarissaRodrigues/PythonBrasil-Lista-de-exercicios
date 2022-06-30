# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

n = int(input("Digite um número: "))
contador = 0

for i in range(1, n+1):
  if n % i == 0:
    contador += 1

if contador > 2:
  print(f"O número {i} não é primo!")
else:
  print(f"O número {i} é um número primo!")
    