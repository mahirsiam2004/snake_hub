name=input("enter your name ")

while name=="":
    print("you did not enter your name")
    name=input("enter your name : ")
    print(f"hello {name }")

# ------------------------------------------

age = int(input("enter your age : "))
while age<0:
        print("age can't be negative")
        age=int(input("enter your age :"))

        print(f"you are {age} years old")

# ------------------------------------------

food=input('enter a food you like (q to quite): ')

while not food =='q':
      print(f"you like {food}")
      food=input('enter another food you like (q to quite): ')
      print("bye")

# ------------------------------------------

num=int(input("enter a #between 1 - 10: "))
while num<1 or num>10:
      print(f"{num} is not valid")
      num=int(input("enter a # between 1-10: "))

print(f"your number is {num}")