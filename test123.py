def countdown(number):
    total= 0
    while number >= 0:
        print (number)
        total+=number 
        number -= 1
    return total 
def main():
    num = int(input("Enter a number: "))
    resultdown = countdown(num)
    print("The sum is: ",resultdown)
main()
