import random
import glob


def intro_pg():
    print(34 * "*")
    print("{:*^34}".format(" Welcome to Hangman Game "))
    print(34 * "*", end=3 * "\n")


def db_theme_list():
    theme_list = []
    for arquivo in glob.glob("*.*"):
        if ".txt" in arquivo:
            theme_list.append(arquivo)
    return theme_list


def theme_words(theme_list):
    print(34 * "-")
    print("{:^34}".format("THEMES"))
    print(34 * "-", end=2 * "\n")
    for n_t in range(len(theme_list)):
        print(" {} - {}".format(n_t, theme_list[n_t]))
        if n_t == (len(theme_list) - 1):
            print(34 * "-", end="\n")
    chosen_theme = int(input("Set the number referring to the theme of the words according to the menu above: "))
    while chosen_theme not in range(len(theme_list)):
        print("Please, choose a valid theme number!")
        chosen_theme = int(input("Set the number referring to the theme of the words according to the menu above: "))
    print("\n")
    print("{:*^34}".format(" LET'S PLAY "), end=3 * "\n")
    return theme_list[chosen_theme]


def read_theme_db(chosen_theme):
    secret_words = []
    with open(chosen_theme) as db_words:
        for line in db_words:
            secret_words.append(line.strip("\n"))
    secret_word = secret_words[random.randrange(0, len(secret_words))].upper()
    return secret_word


def set_list_right_letters(secret_word):
    right_letters = []
    for l_sw in secret_word:
        if l_sw != " ":
            right_letters.append("_")
        else:
            right_letters.append(" ")
    return right_letters


def set_correct_letters(s, sw, rl):
    for l_shot in range(len(sw)):
        if s == sw[l_shot]:
            rl[l_shot] = sw[l_shot]


def print_hangman(error):
    print("  _______     ")
    print(" |/      |    ")

    if error == 1:
        print(" |       -    ")
        print(" |      | |   ")
        print(" |     -----  ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if error == 2:
        print(" |       -    ")
        print(" |      | |   ")
        print(" |     -----  ")
        print(" |      (     ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if error == 3:
        print(" |       -    ")
        print(" |      | |   ")
        print(" |     -----  ")
        print(" |      (_    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if error == 4:
        print(" |       -    ")
        print(" |      | |   ")
        print(" |     -----  ")
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if error == 5:
        print(" |       -    ")
        print(" |      | |   ")
        print(" |     -----  ")
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if error == 6:
        print(" |       -    ")
        print(" |      | |   ")
        print(" |     -----  ")
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if error == 7:
        print(" |       -    ")
        print(" |      | |   ")
        print(" |     -----  ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if error == 8:
        print(" |       -    ")
        print(" |      | |   ")
        print(" |     -----  ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if error == 9:
        print(" |       -    ")
        print(" |      | |   ")
        print(" |     -----  ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if error == 10:
        print(" |       -    ")
        print(" |      | |   ")
        print(" |     -----  ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def winner_message():
    print(3 * "\n")
    print("CONGRATULATIONS!!! YOU WON!!!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def loser_message(sw_loser):
    print(3 * "\n")
    print("Hey life... You were hanged!")
    print("The secret word was {}.".format(sw_loser))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def print_right_letters(rl_p):
    for n_ltrs in range(len(rl_p)):
        print(rl_p[n_ltrs], end=" ")
    print("\n")


def play():
    intro_pg()
    secret_word = read_theme_db(theme_words(db_theme_list()))
    right_letters = set_list_right_letters(secret_word)

    hanged = False
    hit = False
    mistakes = 0
    print_right_letters(right_letters)

    while not hanged and not hit:
        shot = input("Enter a letter or number: ").upper().strip()
        if shot in secret_word:
            set_correct_letters(shot, secret_word, right_letters)
        else:
            mistakes += 1
            print_hangman(mistakes)

        hanged = mistakes == 10
        hit = "_" not in right_letters
        print_right_letters(right_letters)
        print(len("Enter a letter or number:  ") * "-")

    if (hit):
        winner_message()
    else:
        loser_message(secret_word)


play()
