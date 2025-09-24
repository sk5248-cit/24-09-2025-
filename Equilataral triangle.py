a = int(input("Enter the first Side"))
b = int (input("Enter the second side"))
c= int(input("Enter the third side"))
if a ==b and b== c:
    print("equilateral triangle")
elif a==b or b==c or c==a:
    print("Isosceles triangle")
else:
    print("scalene triangle")
