# Ask the user for their name 
Username= input("What is your name?")
# Ask the user for their favourite number
fav_num= int(input("What is your favourite number?") )
# Double, halve and square the user's favourite number
double = fav_num*2 
Halve = fav_num/2
square = fav_num*fav_num

# Greet the user 
print (f"Hey, {Username}, your favourite number is {fav_num}!" )
# Output the results of doubling, halving and squaring their favourite integer
print(f"Double {fav_num} is {double}.")
print(f"Half {fav_num} is {Halve}.")
print(f"{fav_num} squared is {square}.")
print("Bye bye!")