def rectangle(m, n):
   
    for i in range(m):
        print('*' * n)

# Taking input from the user
m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))

# Call the function with user inputs
rectangle(m, n)
