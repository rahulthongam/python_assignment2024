def sum_digits(num):
   
    total = 0
    for digit in str(num):
        total += int(digit)
    return total

num = int(input("Enter a positive integer: "))
result = sum_digits(num)
print("Sum of digits:", result)
