git initimport json
import os 
import random

while True:
    try:
        choose = input("1. write\n2. read\n3 stop\nchoose: ")
        if len(choose) != 1:
            raise ValueError  
    except ValueError:
        print("Please enter one digits only.")
        continue 

    file_name = "rocky.json"
    weapon_option =["rock", "paper", "scissors"]
    if choose == "1":
        user_guess = input("choose your weapon: rock\\paper\\scissors\n ")
        if user_guess not in weapon_option:
            print("Invalid weapon! Please choose rock, paper, or scissors.\n")
            continue
        comp_guess = random.choice(weapon_option)
        if user_guess == "paper" and comp_guess == "rock":
            print(f"you beat {comp_guess} with your {user_guess}")
        elif user_guess == "rock" and comp_guess == "scissors":
            print(f"you beat {comp_guess} with your {user_guess}")
        elif user_guess == "scissors" and comp_guess == "paper":
            print(f"you beat {comp_guess} with your {user_guess}")
        elif user_guess == comp_guess :
            print("game draw")
        else:
            print("you lost")
        
        game_history = {"user_guess": user_guess, "comp_guess": comp_guess}
        if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
            with open(file_name, "r") as file:
                try:
                    data = json.load(file)
                    if not isinstance(data, list):
                        data = [data] 
                except json.JSONDecodeError:
                    data = []
        else:
            data = []
        data.append(game_history)  
        with open(file_name, "w") as file: 
            output = json.dump(data, file, indent = 4)
                
    elif choose == "2":
        if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
            with open(file_name,"r") as file:
                data = json.load(file)
            print(data)
    elif choose == "3":
        print("Goodbye! Thanks for playing.")
        break
    else:
        print("Invalid choice, choose 1, 2, or 3.\n")           
            
                        
        