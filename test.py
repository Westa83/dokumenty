print('No to gramy !!!!')

print('Podaj pierwsza liczbę')
number1 = input()

print('Podaj drugą liczbę')
number2 = input()

print(f'ile to jest: {number1} + {number2}')
result = input()

print(f'jesteś pewna że to: {result}')
answer = input()


if answer == 'tak' and (number1 + number2) == answer:
    print('BRAWO')
elif answer == 'nie' and (number1 + number2) != answer:
    print('MIALAS RACJE')
else:
    print('PUDLO !!!!!')


#komentarz







# bo powinno byc {number1 + liczba2}



