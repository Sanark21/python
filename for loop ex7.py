# Function to display natural numbers and their sum using a for loop
def display_natural_numbers(n):
    sum = 0
    print("The first", n, "natural numbers are:")
    for i in range(1, n + 1):
        print(i, end=" ")
        sum += i
    print("\nSum of first", n, "natural numbers is:", sum)

# Taking input from the user
n = int(input("Enter the value of n: "))
display_natural_numbers(n)
