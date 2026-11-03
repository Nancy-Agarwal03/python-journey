
#ans1

salary = int(input("enter your salary:"))
if (salary<30000):
    print("you have to pay 5% tax")
elif (salary>=30000 and salary<=7000):
    print("you have to pay 15% tex")
elif (salary>70000):
    print("you hve to pay 25% tax")
else:
    print("you don't have to pay tax")




#ans2

a=int(input("enter your first number:"))
b=int(input("enter your ending number:"))
print ("even number between these two are")
for num in range(a,b+1):
    if num%2 == 0:
        print(num)


#ans3,4
n = int(input("enter your number:"))
print("it has digits:")
temp=n
count=0
while temp>0:
    temp=temp//10
    count+=1
divisor = 10**(count-1)
temp=n
while divisor>0:
    digit = temp//divisor
    print(digit)
    temp = temp % divisor
    divisor = divisor//10
print ("total digits:",count)




#ans5
# n= int(input("enter your number"))



