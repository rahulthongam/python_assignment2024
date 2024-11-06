def digital_root(num):
    while num >= 10:
        digit_sum = 0
        for digit in str(num):
            digit_sum += int(digit)
        num = digit_sum
    return num

n = int(input("Enter a number: "))
res = digital_root(n)
print("Digital root of the number is:", res)
