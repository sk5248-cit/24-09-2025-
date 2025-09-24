def is_equilateral(a,b,c):
    if a==b and b==c:
        return "yes"
    else:
        return "No"
a=int(input("Enter side a: "))
b=int(input("Enter side b: "))
c=int(input("Enter side c: "))
print(is_equilateral(a,b,c))
