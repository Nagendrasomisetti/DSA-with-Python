# count number of digits in a number

def count_number_of_digits(n):
    count = 0
    if n == 0:
        return 1
    else:
        while n > 0:
            count +=1
            n //=10
    return count
# Main function to execute the code
def main():
    n = int(input("Enter a number to count its digits: "))
    print("You entered:", n)
    digit_count = count_number_of_digits(n)
    print(f"The number of digits in {n} is: {digit_count}")
    
if __name__ == "__main__":
    main()
