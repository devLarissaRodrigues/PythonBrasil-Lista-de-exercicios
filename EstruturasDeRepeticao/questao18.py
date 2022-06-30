# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

n = int(input("Digite a quantidade de números do conjunto: "))
quantidade = 0
contador = 1
soma = 0
maior = 0
menor = 1000000000000

while quantidade < n:
  numero = float(input(f"Digite o {contador}º número: "))
  contador += 1
  quantidade += 1
  soma += numero
  if numero > maior:
    maior = numero
  if numero < menor:
    menor = numero
    
print(f"Menor número digitado: {menor}")
print(f"Maior número digitado: {maior}")
print(f"Soma dos números digitados: {soma}")