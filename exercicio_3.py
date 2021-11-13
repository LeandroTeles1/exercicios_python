# 3. Desenvolva um Programa em PYTHON usando o comando FOR,
# para imprimir a tabuada de multiplicar de N, informado pelo usuário.

n = int(input('Informe um valor: '))
for i in range(11):
  mult = n * i
  print('{} x {} = {}'.format(n, i, mult))


  