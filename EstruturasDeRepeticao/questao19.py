# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

maior = 0
menor = 10000
soma = 0
contador = 1
termos = 0

while True:
  quantidade = int(input("Digite um número entre 0 e 1000: "))
  if quantidade < 0 or quantidade > 1000:
    print("ERRO! Digite um número válido!")
  else:
    while termos < quantidade:
      numero = float(input(f"Digite o {contador}º número: "))
      contador += 1
      soma += numero
      termos += 1
      if numero > maior:
        maior = numero
      if numero < menor:
        menor = numero
    else:
      break
    
print(f"Menor número digitado: {menor}")
print(f"Maior número digitado: {maior}")
print(f"Soma dos números digitados: {soma}")