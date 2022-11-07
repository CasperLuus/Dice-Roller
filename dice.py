import random

def get_dice_type():
    dice_set = {2, 4, 6, 8, 10, 20, 100}
    dice_type = False

    while dice_type == False:
        dice_type = input("What type of dice would you like to roll? ")
        if dice_type.isnumeric():
            dice_type = int(dice_type)
            if not dice_type in dice_set:
                dice_type = False
                print("That dice is not in the list of valid dice, try again bitch.")
        else:
            print("That is not a valid dice, please try again.")
            dice_type = False

    return dice_type


def get_dice_amount():

    dice_amount = False

    while dice_amount == False:
        dice_amount = input("How many would you like to roll? ")

        if dice_amount.isnumeric():
            dice_amount = int(dice_amount)
            break
        else:
            print("That is not a valid dice, please try again.")
            dice_amount = False

    return dice_amount


def get_dice():

    dice = False

    while dice == False:

        print("What would you like to do? \nIf you want to roll a dice please enter in the following format: roll 1d6")

        dice = input().lower().split(" ")


        if dice[0] == "quit":
            print("Thanks for playing!")
            exit

        elif dice[0] == "roll":

            dice_amount, dice_type = do_roll(dice[1])

            if dice_amount == "false":

                dice = False

        else:

            dice = False

    return dice_amount, dice_type


def do_roll(dice):
    dice_set = {2, 4, 6, 8, 10, 20, 100}

    dice_split = dice.split("d")
    dice_amount = dice_split[0]
    dice_type = dice_split[1]

    if dice_amount.isnumeric() and dice_type.isnumeric():

        dice_type = int(dice_type)
        dice_amount = int(dice_amount)

        if not dice_type in dice_set:
            print("That dice is not in the list of valid dice, try again bitch.")
            return "false", ""

        return dice_amount, dice_type

    else:

        print("That is not a valid dice, please try again.")
        return "false", ""


    


def roll_dice(dice_type, dice_amount):

    print("Rolling " + str(dice_amount) + "d" + str(dice_type) + ".")

    total = 0
        
    for i in range(dice_amount):
        dice_roll = random.randint(1, dice_type)
        total += dice_roll
        print(dice_roll)

    print("TOTAL: " + str(total))
    

if __name__ == "__main__":
    while True:
        dice_amount, dice_type = get_dice()
        roll_dice(dice_type, dice_amount)