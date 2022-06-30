# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

fatorial = 1
n = int(input("Digite um número inteiro: "))

if n < 16 and n > 0:
  for i in range(n, 0, -1):
    fatorial *= i
else:
  print("ERRO! Você deve digitar um número positivo menor que 16")
  n = int(input("Digite um número inteiro: "))

print(fatorial)