sum=0
product=1
count=0

while True:
    integer=int(input("Enter a no.: "))
    sum+=integer
    count+=1
    product*=integer
    ip=input("Press q to quit or press enter to continue")
    if ip=='q':
        break
print("product= ",product,"average= ",sum/count)