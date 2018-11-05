#python program to find the compound interest

principalamt = float(input("Enter the principal amount :"))
time= float(input("Enter the time :")
rate=float(input("Enter the rate of interest")
compound=int(input("Enter the compound times per year")

amount=principalamt*(1+(rate/compound))**(compound*time)
             print("The amound compounded is:",amount)
