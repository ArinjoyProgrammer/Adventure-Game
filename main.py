import random


askingName = input("What is your name? ")
print(f"Welcome {askingName} to the Adventure!")

askForPlay = input("Do you want to play the game (y/n)? ").lower()

if askForPlay == "y".lower():
    print(f"Ok {askingName}, let's start the Adventure!")
else:
    quit()


def story_intro():
    story = "\n\nThe Story:\nYou were a Captain of a Big Ship. You were sailing the ship and suddenly a a huge storm came. You and your friends were shouting 'Help! Help!' But there was no one there to help you and your friends. Suddenly the Ship was sinking and you and your friends became more afraid and then after some minutes the ship sinked! Your all friends died but you were still alive. But how you were alive you also don't know! But you sailed and when you wake up you were on an island!"

    print(story)


def level1():
    storyContinued = "You are on a island where no one was there!\nSo what you want to do now? (explore the island carefully/watch out for some food or fruits/just wait for the night fall)?\n"
    print(storyContinued)
    storyInteraction = input("You: ")

    if storyInteraction == "explore the island carefully".lower():
        print("Result for doing: You went to expore and found a big dark cave!\n\nCongradulations you have passed LEVEL 1")
    elif storyInteraction == "watch out for some food or fruits".lower():
        print("Result for doing: You went on finding some food or some fruits and suddenly a snake came and bite on your toes and you died instantly!! You lose!")
        quit()
    elif storyInteraction == "just wait for the night fall":
        print("Result for doing: Some dangerous zombies came and killed you when you were walking in the night!! You lose!")
        quit()
    else:
        print("Invalid response! You lose!")
        quit()


def level2():
    introMessage = "\nYour LEVEL 2 has been started and now it will be harder to choose what to do!!"
    print(introMessage)

    storyContinued = "You found a big and dark cave but what will you do now in that\n(leave the place/make it like a home)?\n".lower()
    print(storyContinued)
    storyInteraction = input("You: ")

    if storyInteraction == "leave the place".lower():
        print("You left the place and at night some Deadly Zombies came and killed you there!! You lose!")
        quit()
    elif storyInteraction == "make it like a home".lower():
        print("You entered the dark hollow cave and started to build it like your house!\nCongradulations you have passed the PART1 of LEVEL2")
    else:
        print("Invalid response! You lose!")
        quit()



def level3():
    introMessage = "Welcome to LEVEL 3"
    print(introMessage)

    storyContinued = "You were just about starting to make it your own house and then suddenly you remembered that you have to resources! So what will you do now? (go near the ocean to gather some water/gather some materials of wood/gather some food)?\n"
    print(storyContinued)
    storyInteraction = input("You: ")

    if storyInteraction == "go near the ocean to gather some water".lower():
        print("You went near the ocean and gathered some water and drinked that but after some time you felt that the water was salty and then from that day you have some health problems!! You lose!")
        quit()
    elif storyInteraction == "gather some materials of wood".lower():
        print("You gathered some wood and decorated you cave nicely and now it si looking very beautiful!\nCongradulations! You passed the LEVEL3")
    else:
        print("Invalid response!! You lose!")
        quit()


def level4():
    introMessage = "level 4 Comming Soon!"
    print(introMessage)


def level5():
    pass




# Functions Running
story_intro()
level1()
level2()
level3()
level4()
level5()
