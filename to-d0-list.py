import json
import os

while True:
    choose = input("1. write\n2. read\n3 stop\nchoose: ")
    file_name = "list.json"
    if choose == "1":
        key = input("enter the list number: ")
        value = input("enter the list value: ")
    
        if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
            with open(file_name , "r") as file:
                user_input = json.load(file)
        else:
            user_input = {}
        user_input[key] = value
        with open(file_name , "w") as file:
            json.dump(user_input , file, indent = 4)
            print("load data into json")
            
    elif choose == "2":
        if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
            with open(file_name, "r") as file:
                user_input = json.load(file)
            search_key = input("Enter the key you want to read: ")
            if search_key in user_input:
                print({user_input[search_key]})
            else:
                print("Key not found in the list!")
        else:
            print("The file is empty or does not exist yet.")
    elif choose == "3":
        print("bye! have a great day")
        break  
    else:
        print("not a valid function number!")
        
        