from datetime import datetime

for n in range(1, 101):
    if n % 5 == 0 and n % 3 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)

x = 3

print('Fizz' if x % 3 == 0 else n)

wait_until = (datetime.now().second + 2) % 60

while datetime.now().second != wait_until:
    # print('Still waiting')
    # break
    pass
print(f'We are at {wait_until} seconds!')

