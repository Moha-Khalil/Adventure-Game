import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro(enemy):
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here,"
                " and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                " (but not very effective) dagger.\n")


def fight(items, enemy):
    if "sword" in items:
        print_pause(f"As the {enemy} moves to attack,"
                    " you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand"
                    " as you brace yourself for the attack.")
        print_pause(f"But the {enemy} takes one look at your"
                    " shiny new toy and runs away!")
        print_pause(f"You have rid the town of the {enemy}."
                    " You are victorious!")
        play_again()
    else:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {enemy}.")
        print_pause("You have been defeated!")
        play_again()


def field(items, enemy):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    choice = input("What would you like to do?\n(Please enter 1 or 2.)\n")
    if choice == '1':
        house(items, enemy)
    elif choice == '2':
        cave(items, enemy)
    else:
        field(items, enemy)


def house(items, enemy):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens"
                f" and out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")
    if "sword" not in items:
        print_pause("You feel a bit under-prepared for this,"
                    " what with only having a tiny dagger.")
    house_choice = input("Would you like to (1) fight or (2) run away?\n")
    if house_choice == '1':
        fight(items, enemy)
    elif house_choice == '2':
        print_pause("You run back into the field. Luckily,"
                    " you don't seem to have been followed.\n")
        field(items, enemy)


def cave(items, enemy):
    print_pause("You peer cautiously into the cave.")
    if "sword" in items:
        print_pause("You've been here before, and gotten all the good stuff."
                    " It's just an empty cave now.")
        print_pause("You walk back out to the field.\n")
        field(items, enemy)
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger"
                    " and take the sword with you.")
        items.append("sword")
        print_pause("You walk back out to the field.\n")
        field(items, enemy)


def play_again():
    play = input("Would you like to play again? (y/n)\n")
    if play == 'y':
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif play == 'n':
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again()


def play_game():
    items = []
    enemy_creature = ['gorgon', 'pirate', 'troll', 'dragon', 'wicked fairie']
    enemy = random.choice(enemy_creature)
    intro(enemy)
    field(items, enemy)


play_game()
