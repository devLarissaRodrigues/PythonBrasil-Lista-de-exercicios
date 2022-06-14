# Altere o programa anterior para mostrar no final a soma dos números.
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
soma = 0

for numero in range(num1 + 1, num2):
  print(numero)
  soma += numero

print(f"Soma = {soma}")