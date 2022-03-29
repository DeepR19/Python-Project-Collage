# Program to convert Pound to KGs

# Input = 2
# output = 0.9

def poundTo_KG();
    a = int(input("Enter your amount in Pound: "))

    kg = a*.45

    print(a," pound is: ",kg)



# Program to find sum of digit

# Input = 234
# Output = 9

def sumOfDigit();
    a= int(input("Enter a number: "))
    sum=0
    while(a>0):
        a = a%10
        sum += a
        a = a//10
    
    print('Sum of digit is: ',sum)


