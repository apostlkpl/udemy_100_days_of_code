#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
import shutil
import time

names_lst = []

with open("Input/Names/invited_names.txt", "r") as names:
    for name in names:
        name = name.strip()
        names_lst.append(name)
print(names_lst)

for name in names_lst:
    shutil.copy("Input/Letters/starting_letter.txt", "Output/ReadyToSend/"+str(name)+".txt")
    with open("Output/ReadyToSend/"+str(name)+".txt", "r") as letter:
        edited = letter.read()
        edited = edited.replace("[name]", str(name))
        edited = edited.replace("Angela", "Apostolis")
    with open("Output/ReadyToSend/"+str(name)+".txt", "w") as letter:
        letter.write(edited)
    print("Created letter for " + str(name) + ".")
    time.sleep(1)
print("\nCompleted ✓✓")
