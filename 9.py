print('Quantity is ', a)
b = (a * 100)
if b >= 1000:
    print('CONGRATS ! \n \t  You got discount of 10% on purchasing of :', b)
    c = b * (10 / 100)
    print("Your discount is ", c)
    d = b - c
    print('You have to pay only ', d)
else:
    print("You have to pay : ", b)
    print('\n \t "Buy some more to get 10 % discount on purchasing of quantity 10 or more. ',
          "\n \t \"Happy Shopping\" ")
