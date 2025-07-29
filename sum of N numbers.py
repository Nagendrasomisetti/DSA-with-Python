#Finding sum of N numbers
n = int(input("Enter the number of rows:"))
sum_n = 0
for i in range(1,n+1):
    sum_n +=i
print(f"The sum of first {n} numbers is: {sum_n")