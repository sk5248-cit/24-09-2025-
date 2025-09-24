#checking if the number is even or odd
def checking_if_its_even_or_odd():
    num=int(input("Enter the number u want to check if its even or odd= "))
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
#Checking if its positive or negative number
def checking_if_it_is_negative_or_positive(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
#Finding its square
def square_of_the_number(num):
    return num **2 
#Finding its cube
def cube_of_the_number(num):
    return num **3
#printing all the results
def printing_reults(num):
    print("the results we wanted",num)

