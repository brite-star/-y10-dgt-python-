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

        except ValueError:
            print(error)
        return (num)
    
 
# Main routine 
width = test_float_Num("Enter width of your area:")
print(f"The number you have entered is ✨ {width} ✨.")
print("")
length = test_float_Num("Enter length of your area:")
print(f"The number you have entered is ✨ {length} ✨.")
print("")
costpersquaremeter = test_float_Num("Enter the cost per meter squared:")
print(f"The number you have entered is ✨ {costpersquaremeter} ✨.")

#Adding up the numbers
permeter= width + width + length + length
area = width*length
totalcost = area*costpersquaremeter

#Results
print("")
print(f"Thanks,{Username}!")
print("Here are your results:")
print("")
print("✨ r e s u l t s ✨")
print("---------------------------------------")
print("The permeter of your area is: ")
print(f"✨ {permeter} m ✨")
print("")
print(f"The total cost of your area is: ")
print(f"✨ ${totalcost} ✨")
print("----------------------------------------")

#