total_sum = 0

for n in range (10):
    num = float(input('Enter number: '))
    total_sum += num

avg = total_sum / 10

print('Average of numbers = %0.2f' %avg)