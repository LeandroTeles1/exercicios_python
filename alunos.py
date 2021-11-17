alunos = []
media = 0
maior = 0
menor = 0
for i in range(0, 3):
  alunos.append(input('Informe o peso do aluno: '))
  if i == 0:
    maior = menor = alunos[i]
  else:
    if alunos[i] > maior:
      maior = alunos[i]
    if alunos[i] < menor:
      menor = alunos[i]
  media = alunos[i]
  media = media + media
media = media / 3
print('A media dos pesos eh: {}'.format(media))
print('O maior peso informado foi: {}'.format(maior))
print('O menor peso informado foi: {}'.format(menor))
