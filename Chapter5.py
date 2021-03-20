


import time
import global_variables


def Chapter5():
    time.sleep(3)
    #print("She sees an executioner with an axe ready to mutilate someone’s head. She picked up the bow and arrow and released it, killing the man.")
##Player can come into this scene either with "Bow and Arrow" or "Sword" in their Inventory, not both!

    if "Bow and Arrow" in global_variables.Inventory:
        print("Bow and Arrow")
    elif "Sword" in global_variables.Inventory:
        print("Use Sword")

    player_choice = input("A.Turn back, B.Go further into castle")
    while player_choice != "B" and player_choice != "A":

        if player_choice == "A":
            print("Go to Chapter3")
            import Chapter3
            Chapter3.Chapter3()

        elif player_choice == "B":
            print("Go to Chapter6")
            print("Go further into Castle")

    time.sleep(2)
    if player_choice == "A":
        print("Go to Chapter3")
        import Chapter3
        Chapter3.Chapter3()
    else:
        print("She goes upstairs into the tower and looks down at the rainy yet suspiciously quiet tower. She looks up and sees a strange figure, big wings, small red face, long body, huge tail; until she sees the Wren itself. “The Wren of lost souls.")
        import Chapter6
        Chapter6.Chapter6()

#Chapter5()