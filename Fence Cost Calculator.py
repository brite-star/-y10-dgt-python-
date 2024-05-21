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

#Asking for input and loop

Width = int(input("What is the lenght of your area (m)?"))
Length = int(input("Great! Now what is the width of your area (m)?"))
Cost = int(input("Now finally, what is the cost per square meter?")) 

#Giving user the results 
print("")
print(f"Thanks,{Username}!")
print("Here are your results:")
print("")
print("✨ r e s u l t s ✨")
print("------------------------------------------")
print(f"The total perimeter of your area is :")
print ("And you total cost is: ")
print("------------------------------------------")