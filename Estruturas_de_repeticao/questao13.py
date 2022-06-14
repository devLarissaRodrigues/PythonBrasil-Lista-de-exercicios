# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input("Digite a base: "))
expoente = int(input("Agora digite o expoente: "))
base_fixa = base

if expoente == 1:
  print(f"Todo número elevado a 1 é igual a ele mesmo, logo, é igual a {base}")

elif expoente == 0:
  print("Todo número elevado a 0 é igual a zero")

elif expoente < 0:
  for num1 in range(1, abs(expoente)):
    base = base * base_fixa
    print(1/base)
  
else:
  for num2 in range(1, expoente):
    base = base * base_fixa
    print(base)
  