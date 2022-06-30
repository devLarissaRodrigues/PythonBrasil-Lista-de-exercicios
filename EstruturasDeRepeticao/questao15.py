# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

t1 = 0
t2 = 1
n = int(input("Digite o n-ésimo termo da série de Fibonacci: "))
print(t2, end=" ")

while True:
  t3 = t1 + t2
  if t3 <= n:
    print(t3, end=" ")
    t1 = t2
    t2 = t3
  else:
    break
