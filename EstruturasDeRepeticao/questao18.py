# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

quantidade = int(input("Digite a quantidade de número do conjunto: "))
maior = 0
menor = 100000000000
soma = 0

while quantidade > 0:
  numero = int(input("Digite um número: "))
  quantidade -= 1
  soma += numero
  if numero > maior:
    maior = numero
  if numero < menor:
    menor = numero

print("=" * 45)
print(f"Soma = {soma}")
print(f"Maior número = {maior}")
print(f"Menor número = {menor}")