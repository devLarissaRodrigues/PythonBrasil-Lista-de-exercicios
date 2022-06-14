# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0

for indice in range(1,6):
  numero = float(input(f"Digite o {indice}º número: "))
  soma += numero

media = soma/5

print(f"A soma dos números digitados é {soma} e a média entre eles é {media:.2f}")


  
  
  



