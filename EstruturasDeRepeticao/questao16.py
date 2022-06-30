# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
t1 = 0
t2 = 1
print(t2, end=" ")

while True:
  t3 = t1 + t2
  if t3 > 500:
    print(t3, end=" ")
    break
  else:
    print(t3, end=" ")
    t1 = t2
    t2 = t3