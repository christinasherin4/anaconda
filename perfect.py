num = int(input("Please give first number a:"))
sum = 0
for i in range(1,(num//2)+1):
    remainder=num%i
    if remainder==0:
        sum=sum+i
if sum == num:
    print("Given number is perfect number")
else:
    print("Given number is not a perfect number")