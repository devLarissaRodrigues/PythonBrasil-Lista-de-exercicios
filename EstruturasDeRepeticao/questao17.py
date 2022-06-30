# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

fatorial = int(input("Digite um número inteiro para calcularmos o fatorial: "))

print(f"{fatorial}!=", end="")
contador = fatorial - 1
resultado = 1

for numero in range(fatorial, 0, -1):
  if numero == 1:
    print(f"{numero}", end="") 
  else:
    print(f"{numero}.", end="")
    resultado *= numero
    contador -= 1
  
print(f"={resultado}", end="")