i = 0
result  = 0
n = int(input("please give a number: "))
num1 = n
temp = n
while(n!=0):
    n=(n//10)
    i=i+1
while num1!=0:
    n=num1%10
    result=result+pow(n,i)
    num1=num1//10
if temp==result:
    print("Number is armstrong")
else:
    print("number is not armstrong")