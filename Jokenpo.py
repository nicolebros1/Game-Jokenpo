from random import randint
from time import sleep

opcoes = ('pedra','papel','tesoura')
pc = randint(0,2)
print ('''opcoes: 
[0] Pedra
[1] Papel
[2] Tesoura''')
Player = int (input('digite a opção da sua jogada:'))
print ("JO")
sleep(1)
print('KEN')
sleep(1)
print ('PO')
sleep (1)
print('-='*22)
print(f'Computador:{opcoes[pc]}')
print(f'Você:{opcoes[Player]}')
print('-='*22)
if pc == 0:
    if Player == 0:
        print('Empatou')
    elif Player == 1:
        print('Você venceu')
    elif Player == 2:
        print('Você perdeu')

if pc == 1:
    if Player == 1:
        print ('Empatou')
    if Player == 0:
        print('Você perdeu')
    if Player == 2:
        print('Você Venceu ')

if pc == 2:
    if Player == 1:
        print('Você perdeu')
    if Player == 2:
        print('Empatou')
    if Player == 0:
        print('Você venceu')