


import time
import global_variables

def Chapter4():
    time.sleep(3)
    print("She climbs the narrow stairs up to the tower")

    player_choice = input("Climb stairs A.Yes, B.No")

    if player_choice == "A":
        print("Climb Stairs")
        print("Gets bow and arrow as a bonus for showing courage, to save the man.")
        global_variables.Inventory.append("Bow and Arrow")

    elif player_choice == "B":
        print("Gets a sword")
        global_variables.Inventory.append("Sword")

    #global_variables.Health -= 3
        ##Takes away 3 from the Health variable ( It is used to track damage to the player in fights!)
    #global_variables.Health += 3
        ##Adds 3 to the Health variable (It is used to track healing for the player!)
    #print(global_variables.Inventory)
    #import Chapter5

    import Chapter5
    Chapter5.Chapter5()