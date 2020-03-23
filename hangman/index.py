from random import randint

def hanfman(*words):

    word = words[randint(0, len(words)-1)]
    wrong = 0
    stages = ["",
              "________             ",
              "|                    ",
              "|         |          ",
              "|         O          ",
              "|        /|\\        ",
              "|        / \\        ",
              "|                    ",
              ]
    rlettes = list(word)
    board = ["_"] * len(word)
    win = False
    print('Добро пожаловать на казнь!')
    while wrong < len(stages) - 1:
        print('\n')
        msg = 'Введите букву: '
        char = input(msg)
        if char in rlettes:
            cind = rlettes.index(char)
            board[cind] = char
            rlettes[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print('Вы выиграли')
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print('Вы проиграли')

hanfman('мир', 'кот', 'прах')