# Ask user for width and loop until they enter a number that us more than zero
error = "Please enter a number that is more than zero\n"
while True:

    
    width = float(input("width: "))
    if width > 0: 
        break

else: 
    print(error) 