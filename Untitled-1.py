def countup(number):
    total = 0
    i = 1
    while i <= number:
        print(i)
        total += i
        i += 1
    return total

# Call the function
result = countup(99)
print("Total:", result)

