# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
sexo = input("Digite seu sexo (f ou m): ")
estado_civil = input("Digite seu estado civil (s, c, v, d): ")


while True:
  print("-" * 40)
  if len(nome) > 3:
    print("Nome válido!")
  else:
    print("Nome inválido!")

  if idade >= 0 and idade <= 150:
    print("Idade válida!")
  else:
    print("Idade inválida!")

  if salario > 0:
    print("Salário válido!")
  else:
    print("Salário inválido!")

  if sexo == "f" or sexo == "m":
    print("Sexo válido!")
  else:
    print("Sexo inválido!")

  if estado_civil == "s" or estado_civil == "c" or estado_civil == "v" or estado_civil == "d":
    print("Estado civil válido!")
  else:
    print("Estado civil inválido")
  break
    