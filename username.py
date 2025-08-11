username=input("enter your username")
if len(username)>12 :
    print("your username can't be more than 12 characters")

elif not username.find(" ")==-1 :
    print("your user name can't contain spaces")
elif not username.isalpha() :
    print("your user name can't contain numbers")

else:
    print(f"welcome {username}")