##booleans
print(f"a: {20 > 9}")
print(f"b: {30 == 31}")
print(f"is 40 not equal to 40: {40 != 40}")
print(f"The remainder of 5 divided by 2: {5%2}")
print(f"6//4: {6//4}")

##variables and literals
myName = "Kyler"
myAge = 21
print(f"a: {39}")
print(f"b: {"Hi"}")
print(f"c: {True}")
print(f"d: {myName}")
print(f"e:{myAge}")


##precedence
print((1+2)*(4-2))
print(1+2*4-2)

##relational operators
print(f"is Kyler = Kyle: {'Kyler' == 'Kyle'}" )

##equality operator
myDogsName = "Lilly"
print(myDogsName == "Bella")

#comparison operators
print("comparison:" " bb" < "cc")
print("comparison:", 8 > 4)
a = 50
b = 60
print(f"comparison: {a} is greater than {b}" if a>b else"")
print(f"comparison: {a} is equal to {b}" if a == b else"")
print(f"comparison: {a} is less than {b}" if a < b else"")

#if, else, elif
bank_balance = 45
if bank_balance <100:
    print("Your bank balance is low!")
elif bank_balance >100:
    print("Your bank balance is ight")
else:
    print("Your bank balance is high")

money = 150
if money > 150:
    money+=200
elif money < 100:
    money-=50
else:
    print("You have beetween $100 and $150")

##ternary operator
fuel = 9
print("fuel tank now" if fuel <=2 else "Our fuel is sufficient")

##While and for loops
while fuel > 1:
    #keep driving
    print("Theres enough fuel")
    fuel -= 1

books = ['lord of the rings', 'Harry Potter', 'It']
for book in books:
    print(f"book: {book}")



for count in range(15):
    print(f"{count} times 12 is {count * 12}")
    if count == 7:
        break


