
import time

def Chapter2():
    time.sleep(2)
    print("As she is sleeping blissfully, she hears a loud wind that opens her window. She searches the room")

    player_choice = input("Do you want to A.Search the room, B.Go back to sleep, or C.Close the window?")
    while player_choice != "B":

        if player_choice == "A":
            print("Search the room")
            player_choice = input("Perform an action")

        elif player_choice == "B":
            print("Go back to sleep")

        elif player_choice == "C":
            print("Close the window")
            player_choice = input("Perform an action")

        else:
            print("Answer not recognized, please type in A, B, or C.")
            player_choice = input("Perform an action")

    time.sleep(3)
    print("She tries to go back to sleep as she is frightened of the darkness in her room")
    print("In her dream, she sees a large castle and she enters it.")

    import Chapter3
    Chapter3.Chapter3()