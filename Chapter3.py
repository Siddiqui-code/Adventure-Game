



import time

def Chapter3():
    time.sleep(2)
    print("Castle door opens in front of her")

    player_choice = input("Do you want to open the door? A.Yes, B.No")
    while player_choice != "A":

        if player_choice == "A":
            print("Open the door")

        elif player_choice == "B":
            print("Go back to sleep")
            player_choice = input("Perform an action")

        else:
            print("Answer not recognized, please type in A or B.")
            player_choice = input("Perform an action")

    time.sleep(3)



    import Chapter4
    Chapter4.Chapter4()