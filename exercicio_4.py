# Faça um programa em python para converter a temperatura
# de graus centígrados em fahrenheit, usando a fórmula
# abaixo. Se a temperatura em centígrados for abaixo de
# 10 ou acima de 35 informar "PERIGO" se não informar "OK".
# F = 32+(9/5)*C

c = int(input('Informe a temperatura em Centígrados: '))
f = 32+(9/5)*c
print('Temperatura convertida em Fahrenheit: {}'.format(f))
if c < 10 or c > 35:
  print('PERIGO!')
else:
  print('OK')

