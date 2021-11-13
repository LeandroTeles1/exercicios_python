# 2. Desenvolva um Programa em PYTHON usando o comando FOR,
# para calcular e imprimir o fatorial de N, informado pelo usuário.

fatorial = 1
valor = int(input('Digite um valor inteiro: '))
valor = valor + 2
for i in range(2, valor):
  cont = i - 1
  fatorial = cont * fatorial
  print(cont)
valor = valor -2
print('O fatorial de {} eh {}.'.format(valor, fatorial))

