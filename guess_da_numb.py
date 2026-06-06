import random
import json
import os

while True:
    user = input("1. play\n2. stop\nchoose: ")
    pic = "use.json"
    if user == "1":
        user_guess = int(input("guess the number: "))
        comp_guess = random.randint(1,10)
        if user_guess == comp_guess:
                print("yess")
        else:
                print("nope")
        print("user guess: ",user_guess)
        print("computer guess: ",comp_guess)        
        game_data = {"user_guess": user_guess, "comp_guess": comp_guess}
                
        if os.path.exists(pic) and os.path.getsize(pic) > 0:
            with open(pic, "r") as file:
                try:
                    data = json.load(file)
                    if not isinstance(data, list):
                        data = [data]  
                except json.JSONDecodeError:
                    data = []
        else:
            data = []
        data.append(game_data) 
        with open(pic, "w") as file: 
            output = json.dump(data, file, indent = 4)
    elif user == "2":
        print("have a great dayy")
        break
    else:
        print("stupid")
        break
            
         
    
  