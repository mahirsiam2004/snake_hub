import math

# print(math.pi)
print(math.e)


x=3.1416
y=-9
z=40

# result=round(x)
# result=abs(y)
# result=pow(4,3)
# result=max(x,y,z)
# result=min(x,y,z)
# result=math.sqrt(x)
# result=math.ceil(x)
result=math.floor(x)

# print(result)


radius=float("Enter the radius of a circle: ")
ans=2*math.pi *radius
print(f"the ans is :{round(ans,2)}cm")


a= float(input("enter side a : "))
b= float(input("enter side b : "))
c=math.sqrt(pow(a,2) + pow(b,2))

print(f"side c ={c}")