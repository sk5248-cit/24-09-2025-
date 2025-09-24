def sum_of_odds():
    total= 0
    while True:
        num = int(input("Enter a number (o to stop)"))
        if num == 0:
            break 
        if num % 2 == 0:
            continue
        total += num
    print("Sum of odd numbers: ",total)
sum_of_odds()