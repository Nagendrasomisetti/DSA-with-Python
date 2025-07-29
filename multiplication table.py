# Print multiplication table
def multiplication_table(n):
    for i in range(1, n + 1):
        print(f"{n} * {i} = {n * i}")

# Main function to execute the code
def main():
    n = int(input("Enter the number for multiplication table: "))
    print("You entered:", n)
    multiplication_table(n)

if __name__ == "__main__":
    main()