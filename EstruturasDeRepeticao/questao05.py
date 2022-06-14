#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

populacao_a = int(input("Digite a população do país A: "))
taxa_a = float(input("Digite a taxa de crescimento da população A: "))
populacao_b = int(input("Digite a população do país B: "))
taxa_b = float(input("Digite a taxa de crescimento da população B: "))
anos = 0

while True:
  calculo_a = populacao_a + (populacao_a * taxa_a)
  calculo_b = populacao_b + (populacao_b * taxa_b)
  populacao_a = calculo_a
  populacao_b = calculo_b
  anos += 1
 
  if (calculo_a >= calculo_b):
    print(f"Em {anos} anos, a população do país A: {populacao_a:.2f} se iguala ou se torna superior à população do país B: {populacao_b:.2f}")
    break