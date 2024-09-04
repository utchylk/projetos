from random import choice
senha_tamanho = int(input('Que tamanho você deseja que seja sua senha? '))
caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '$', '%', '&', '*']
senha = ''
for c in range(senha_tamanho):
    senha += choice(caracteres)
print(f'A senha gerada é {senha}')