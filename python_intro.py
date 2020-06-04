""" print('hello, django girls')

if 3 > 2:
  print('Funciona!')

if 5 > 2:
  print('5 é maior que 2')
else:
  print('5 não é maior que 2')

name = 'Sonja'
if name == 'Van':
  print('Olá Van')
elif name == 'Sonja':
  print('Olá Sonja')
else:
  print('olá estranho!')

volume = 57
if volume < 20:
  print('está um baixo')
elif 20 <= volume < 40:
  print('está bom para música ambiente')
elif 40 <= volume < 60:
  print('perfeito, posso ouvir todos os detalhes')
elif 60 <= volume < 80:
  print('está muito alto!')
else:
  print('meus ouvidos doem! :(')

def hi():
  print('olá')
  print('tudo bem?')

hi()

def hi(name):
  if name == 'van':
    print('olá van')
  elif name == 'sonja':
    print('olá sonja')
  else:
    print('olá estranho') 

hi('estela')"""


def hi(name):
  print('olá ' + name + '!')

girls = ['rachel', 'monica', 'phoebe', 'van', 'you']
for name in girls:
  hi(name)
  print('próxima')

for i in range(1, 6):
  print(i)
