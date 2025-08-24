# list =[]
# set  = {}
# tuple=()

fruits=["apple", "orange", "banana","coconat"]

# print(fruits[0])
# print(dir(fruits))
# print(help(fruits))
print(len(fruits))
print("apple" in fruits)

fruits[0]="pineapple"
fruits.append("pineapple")
# fruits.remove("apple")
fruits.sort()
fruits.insert(0, "kola")
fruits.reverse()
fruits.clear()
# fruits.add("bal")
print(fruits.index("apple"))
print(fruits.count("apple")) 

for fruit in fruits:
    print(fruit)