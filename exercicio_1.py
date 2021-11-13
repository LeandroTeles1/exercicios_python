# 1. Desenvolva um Programa em PYTHON usando o comando FOR,
# para imprimir os números pares de 0 a 100 e a soma destes números.

soma = 0
for i in range(0, 101):
  valor = i%2
  if valor == 0:
    print(i)
    soma = soma + i
print(soma)

