import random

# Write your code here

score = {}
name = input("Enter your name: ")
print(f"Hello, {name}")

with open("rating.txt", "r") as f:
    for i in f.readlines():
        i.split(" ")[1].rstrip("\n")
        score[i.split(" ")[0]] = int(i.split(" ")[1])

if name not in score:
    score[name] = 0

def classic():
    while True:
        option = ["scissors", "paper", "rock"]
        computer_option = random.choice(option)
        player_option = input()
        if player_option in option:
                if player_option == computer_option:
                    print(f"There is a draw ({computer_option})")
                    score[name] += 50
                else:
                    if player_option == "rock" and computer_option == "scissors":
                        print(f"Well done. The computer chose {computer_option} and failed")
                        score[name] += 100
                    elif player_option == "scissors" and computer_option == "paper":
                        print(f"Well done. The computer chose {computer_option} and failed")
                        score[name] += 100
                    elif player_option == "paper" and computer_option == "rock":
                        print(f"Well done. The computer chose {computer_option} and failed")
                        score[name] += 100
                    elif player_option == "rock" and computer_option == "paper":
                        print(f"Sorry, but the computer chose {computer_option}")
                    elif player_option == "scissors" and computer_option == "rock":
                        print(f"Sorry, but the computer chose {computer_option}")
                    elif player_option == "paper" and computer_option == "scissors":
                        print(f"Sorry, but the computer chose {computer_option}")
        elif player_option == "!exit":
            print("Bye!")
            break
        elif player_option == "!rating":
            print(f"Your rating: {score[name]}")
        else:
            print("Invalid input")


def customize(x):
    option = x.split(",")
    length = len(option) // 2
    while True:
        computer_option = random.choice(option)
        stronger_than_computer = option[option.index(computer_option) + 1:]
        if len(stronger_than_computer) < length:
            stronger_than_computer.extend(option[:length - len(stronger_than_computer)])
        elif len(stronger_than_computer) > length:
            stronger_than_computer = stronger_than_computer[:length]
        player_option = input()
        if player_option in option:
                if player_option == computer_option:
                    print(f"There is a draw ({computer_option})")
                    score[name] += 50
                elif player_option in stronger_than_computer:
                    print(f"Well done. The computer chose {computer_option} and failed")
                    score[name] += 100
                else:
                    print(f"Sorry, but the computer chose {computer_option}")
        elif player_option == "!exit":
            print("Bye!")
            break
        elif player_option == "!rating":
            print(f"Your rating: {score[name]}")
        else:
            print("Invalid input")



def game():
    game_method = input()
    print("Okay, let's start")
    if game_method == "":
        classic()
    else:
        customize(game_method)
    with open("rating.txt", "w") as f:
        for i, j in score.items():
            f.writelines(f"{i} {j}\n")

game()
