"""
Jogo da Velha com dicionário
"""

the_board = {'top_L': '', 'top_M': '', 'top_R': '',
             'mid_L': '', 'mid_M': '', 'mid_R': '',
             'bot_L': '', 'bot_M': '', 'bot_R': ''
}

def printBoard(board):
    print(board['top_L'] + '  |  ' + board['top_M'] + '  |  ' + board['top_R'])
    print('           ')
    print('-----------')
    print(board['mid_L'] + '  |  ' + board['mid_M'] + '  |  ' + board['mid_R'])
    print('           ')
    print('-----------')
    print(board['bot_L'] + '  |  ' + board['bot_M'] + '  |  ' + board['bot_R'])

vez = 'X'

for i in range(9):
    printBoard(the_board)
    print('A vez é do ' + vez + '. Dê o próximo movimento:')
    move = input()
    the_board[move] = vez
    if vez == 'X':
        vez = '0'
    else:
        vez = 'X'

printBoard(the_board)
