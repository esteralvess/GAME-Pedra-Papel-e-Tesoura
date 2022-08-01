from random import randint
from time import sleep
itens = ('Pedra', 'Papel','Tesoura')
computador = randint(0,2)
jogador = int(input(f'''Sua opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA

Qual é a sua jogada? '''))

print(f'''
{'=' * 25}
O computador jogou {itens[computador]} 
Jogador jogou {itens[jogador]}
{'=' * 25}''')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)

print('='*25)

if computador == 0:
	if jogador == 0:
		print("EMPATE!")
	elif jogador == 1:
		print('VOCÊ GANHOU!')
	elif jogador ==2:
		print('O COMPUTADOR ganhou!')
	else:
		print('JOGADA INVÁLIDA!')

elif computador == 1:
	if jogador == 0:
		print('O COMPUTADOR ganhou!')
	elif jogador == 1:
		print('EMPATE!')
	elif jogador ==2:
		print('VOCÊ GANHOU!')
	else:
		print('JOGADA INVÁLIDA!')
		
elif computador == 2:
	if jogador == 0:
		print('VOCÊ GANHOU!')
	elif jogador == 1:
		print('O COMPUTADOR ganhou!')
	elif jogador ==2:
		print('EMPATE!')
	else:
		print('JOGADA INVÁLIDA!')

print('='*25)