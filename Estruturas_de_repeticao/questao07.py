# Faça um programa que leia 5 números e informe o maior número.

maior = 0

for indice in range(1, 6):
  numero = float(input(f"Digite o {indice}º número: "))
  if numero > maior:
    maior = numero

print(f"O maior número digitado foi: {maior:.2f}")
  
  
  
  