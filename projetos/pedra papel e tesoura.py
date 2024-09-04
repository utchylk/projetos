import random
from time import sleep
cores = ('\033[m', #0- sem cores
     '\033[31m', #1 - vermelho
     '\033[32m', #2 - verde
     '\033[33m', #3 - amarelo
     '\033[34m', #4 - azul
    '\033[35m', #5 - roxo
    '\033[36m', #6 - ciano
    '\033[37m', #7 - cinza
    )


def ponto(pontinho): #Função para dar um tempo de uma linha à outra
    for p in range(0, 3):
        print(pontinho, end='')
        sleep(0.4)


def jogar(msg):
    jogo = ['PEDRA', 'PAPEL', 'TESOURA']

    while True:
        print(f'{cores[4]}-{cores[0]}' * len(msg))
        print(f'{cores[3]}', msg, f'{cores[0]}')
        print(f'{cores[4]}-{cores[0]}' * len(msg))
        jogador = str(input(f'Quer jogar {cores[7]}PEDRA, {cores[2]}PAPEL{cores[0]} ou {cores[6]}TESOURA{cores[0]}? ')).upper().strip()
        if jogador not in jogo:
            print(f'Resposta inválida. Digite {cores[7]}PEDRA, {cores[2]}PAPEL{cores[0]} ou {cores[6]}TESOURA{cores[0]} e tente novamente.')
            sleep(1)
            continue
        computador = random.choice(jogo)
        ponto('.')
        print(f'\nVocê escolheu {jogador}')
        ponto('.')
        print(f'\nO computador escolheu {computador}')

        if jogador == computador:
            sleep(0.5)
            print(f'{cores[4]}EMPATE!')
        elif jogador == 'PEDRA' and computador == 'TESOURA' or jogador =='PAPEL' and computador =='PEDRA' or jogador == 'TESOURA' and computador =='PAPEL':
            sleep(0.5)
            print(f'{cores[2]}Você ganhou!')
        else:
            sleep(0.5)
            print(f'{cores[1]}O computador ganhou!')

        sleep(2)
        while True:
            resposta = str(input(f'{cores[2]}Deseja jogar novamente? [S/N] ')).upper().strip()
            if resposta == 'S':
                break
            elif resposta == 'N':
                return
            else:
                print(f'{cores[1]}Resposta inválida, tente novamente. Por favor, digite "S" ou "N"')
                sleep(1)


jogar('JOGO DE PEDRA PAPEL E TESOURA')
print(f'{cores[6]}Jogo encerrado!')
