


import time
import global_variables

def Chapter6():
    time.sleep(2)
    print("She sees the Wren, shocked of its size. The Wren explodes with a bright light which faded")
    print("Finally, all the souls trapped were released.")

    #player_choice = input("A.Use Bow and arrow, B.Use Cannon")
    Wren_defeated = False
    #global_variables.Inventory.append("Bow and Arrow")
    while Wren_defeated == False and global_variables.Health > 0:
        player_choice = input("A.Use Bow and arrow, B.Use Cannon")
        if player_choice == "A":
            if "Bow and Arrow" not in global_variables.Inventory:
                print("You do not have Bow and Arrow")
                global_variables.Health -= 10
                print(global_variables.Health)
            else:
                print("Pick up Bow and Arrow and kill the Wren")
                Wren_defeated = True

        elif player_choice == "B":
            print("use the canon to win")
            Wren_defeated = True


        else:
            print("Invalid input")
            global_variables.Health -= 10
    if global_variables.Health <= 0:
        print("Game Over")
    elif Wren_defeated == True:
        print("Player wins!")


#Chapter6()






