def print1(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()
def print2(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print()
def print3(n):
    for i in range(1,n+1):
        for j in range(i):
            print(j+1,end="")
        print()
def print4(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end="")
        print()
def print5(n):
    for i in range(1,n+1):
        for j in range(n):
            print("*", end="")
        print()

# Main function to execute the code
def main():
    n = int(input("Enter the number of rows: "))
    print("You entered:", n)
    print5(n)
main()