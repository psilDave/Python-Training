import random


def play():
    level = None
    game_points = 1000
    print(34 * "*")
    print("{:*^34}".format(" Welcome to Guessing Game "))
    print(34 * "*", end=3 * "\n")
    print("What is the difficulty level? ")

    print(" (1) - Easy", " (2) - Medium", " (3) - Hard", sep="\n", end=2 * "\n")
    level = int(input("Define the level:  "))

    while level != 1 and level != 2 and level != 3:
        print("Please, choose a valid level!")
        level = int(input("Define the level:  "))

    if level == 1:
        total_attempts = 20
    elif level == 2:
        total_attempts = 10
    else:
        total_attempts = 5

    secret_number = random.randrange(1, 101)
    print("\n")
    print("{:*^34}".format(" LET'S PLAY "), end=3 * "\n")

    for rounds in range(1, total_attempts + 1, 1):
        print("Attempt {1} from {0}:".format(total_attempts, rounds))
        shot = int(input("Enter a number between 1 to 100: "))
        print("You entered the number: {}".format(shot))

        if shot < 1 or shot > 100:
            print("YOU MUST ENTER A NUMBER IN THE RANGE 1 to 100!")
            print(len("YOU MUST ENTER A NUMBER IN THE RANGE 1 to 100!") * "-")
            continue
        if shot == secret_number:
            print("YOU'RE RIGHT!! CONGRATULATIONS!!")
            print("Your score is: {}".format(game_points))
            print("THE SECRET NUMBER IS: {}.".format(secret_number))
            print(len("THE SECRET NUMBER IS: {}.") * "-")
            break
        else:
            if (shot < secret_number):
                print("You missed... Your shot was smaller than the SECRET NUMBER!")
                print(len("You missed... Your shot was smaller than the SECRET NUMBER!") * "-")

            elif (shot > secret_number):
                print("You missed... Your shot was bigger than the SECRET NUMBER!")
                print(len("You missed... Your shot was bigger than the SECRET NUMBER!") * "-")
            game_points = game_points - abs(secret_number - shot)

    if shot != secret_number:
        print("THE SECRET NUMBER IS: {}.".format(secret_number), end=2 * "\n")
        print(34 * "*")
        print("{:^34}".format("GAME OVER"))
        print(34 * "*")


if __name__ == "__main__":
    play()
