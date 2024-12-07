import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def game():
    limpa_tela()
    print('Bem-vindo ao jogo da forca! \n')
    print('Adivinhe a palavra abaixo:\n')

    palavras = ['banana', 'abacate', 'horta']
    palavra_game = random.choice(palavras)
    letras_descobertas = ['_' for letra in palavra_game]
    chances = 6
    letras_erradas = []

    while chances > 0:
        print('Palavra: ' + ' '.join(letras_descobertas))
        print(f'Chances restantes: {chances}')
        print('Letras erradas: ' + ' '.join(letras_erradas))

        tentativa = input('\nDigite uma letra: ').lower()

        if tentativa in palavra_game:
            for index, letra in enumerate(palavra_game):
                if tentativa == letra:
                    letras_descobertas[index] = letra
        else:
            chances -= 1
            letras_erradas.append(tentativa)
        
        # Verifica se o jogador ganhou
        if '_' not in letras_descobertas:
            print('\nParabéns! Você venceu o jogo. A palavra era:', palavra_game)
            break
    else:
        # Condição de derrota
        print('\nVocê perdeu. A palavra era:', palavra_game)

if __name__ == "__main__":
    game()
    print('\nVocê finalizou o jogo!')