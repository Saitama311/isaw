basket = []

print ("catch any of these fruits: ('apple' , 'orange' , 'mango' , 'guava')")

sui = int(input("How many fruits would you like to catch? "))

print ("Choose a fruit to catch. Press A, O, M, or G.")

for Sha in range(sui):
    Sha += 1
    fruits = input("Fruit "+ str(Sha) + " of " + str(sui) + ":")
    
    if fruits.upper() == "A":
        basket.append("apple")
    elif fruits.upper() == "O":
        basket.append("orange")
    elif fruits.upper() == "M":
        basket.append("mango")
    elif fruits.upper() == "G":
        basket.append("guava")

print("Your basket now has: " + str(basket))

z = 0;

while z < len(basket):
    ip = input("Press E to eat a fruit: ")
    
    if (ip.upper() =="E"):
        basket.pop()
        print("Fruit(s) in the basket : " + str(basket))
print("No More Fruits")        
        