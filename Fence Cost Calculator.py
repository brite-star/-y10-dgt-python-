#Fence Cost Calculator

#Title
print("")
print("✨ f e n c e   c o s t   c a l c u l a t o r ✨")
print("")

#Greet the user
print("Welcome, user!")
print("")

#Asking user for their name
Username= input("What is your name?")
print(f"Hey, {Username}!")
print("Here is how to use this programme:")
print("")

#Instructions
print("✨ i n s t r u c t i o n s ✨")
print("---------------------------------------")
print("Please input: Width and length (m) of ")
print("the area you'll be fencing as well as ")
print("the cost per meter squared.") 
print("--------------------------------------")
print("")

#Creates function to call every time I ask a user for a number 
def test_float_Num(question): 
    done = False 
    error = "Thats an invalid number."
    while not done: 
        print(question)
        try: 
            num = float(input())
            if num > 0:
                return num
            else:
                print(error)

        except ValueError:
            print(error)
        
    
 
# Main routine
done = ""
while done == "":
    width = test_float_Num("Enter width of your area:")
    print(f"The number you have entered is ✨ {width} ✨.")
    print("")
    length = test_float_Num("Enter length of your area:")
    print(f"The number you have entered is ✨ {length} ✨.")
    print("")
    costpersquaremeter = test_float_Num("Enter the cost per meter squared:")
    print(f"The number you have entered is ✨ {costpersquaremeter} ✨.")
    
    #Adding up the numbers
    perimeter= (width + length)*2
    totalcost = perimeter*costpersquaremeter
    
    #Results
    print("")
    print(f"Thanks,{Username}!")
    print("Here are your results:")
    print("")
    print("✨ r e s u l t s ✨")
    print("---------------------------------------")
    print("The permeter of your area is: ")
    print(f"✨ {perimeter} m ✨")
    print("")
    print(f"The total cost of your area is: ")
    print(f"✨ ${totalcost} ✨")
    print("----------------------------------------")
    done = input("If you would like to do another calculation, please press <enter> or any other key to quit.")

print("Thanks for using my fence calculator. Have a nice day!")

