l=int(input("Enter the lowest range "))
h=int(input("Enter the highest range "))
for num in range (l,h +1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)