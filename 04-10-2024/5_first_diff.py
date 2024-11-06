def first_diff(str1, str2):
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            return i
   
    if len(str1) != len(str2):
        return min(len(str1), len(str2))
    return -1

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
result = first_diff(str1, str2)
print("First difference at index:", result)
