alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
nato = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", 
        "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", 
        "Yankee", "Zulu"]

input_on = True

while input_on:
    
    name = input("What is your name?\n").lower()
    speller = []
    
    if name == "exit":
        input_on = False
        print("Now exiting...")
        printer = False
    else:
        for letter in name:
            if letter not in alpha:
                print("Invalid character.")
                printer = False
                break
            else:
                ind = alpha.index(letter)
                speller.append(nato[ind])
                printer = True
    if printer:
        print(speller)
        
