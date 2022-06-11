# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento

populacao_a = 80000
taxa_a = 0.03
populacao_b = 200000
taxa_b = 0.015
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
    




