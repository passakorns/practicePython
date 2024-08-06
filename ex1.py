import random

def input_data():
    pay = int(input('ค่าโดยสารต่อคน >>> '))
    person = int(input('จำนวนคน >>> '))
    print('รายการแสดงรคาค่าโดยสาร')
    for x in range(1,person+1):
        print(f'{pay} * {x} = {pay*x}')


def guess_sum1():
    num1 = random.randint(10,20)
    num2 = random.randint(10, 20)
    message = f'What is {num1} + {num2}? '
    ans_user = int(input(message))
    ans_com = num1 + num2
    output = f'{num1} + {num2} = {ans_com} is {ans_user==ans_com}'
    print(output)

def guess_sum2():
    correct = 0
    for _ in range(10):
        num1 = random.randint(10,20)
        num2 = random.randint(10, 20)
        message = f'What is {num1} + {num2}? '
        ans_user = int(input(message))
        ans_com = num1 + num2
        output = f'{num1} + {num2} = {ans_com} is {ans_user==ans_com}'
        print(output)
        if ans_com == ans_user:
            correct += 1
    print(f'คุณทายถูก {correct} ข้อ จากทั้งหมด 10 ข้อ')


def lucky_seven():
    message=f'Enter amount of money that to play: '
    money = int(input(message))
    move_on = 'y'
    while move_on == 'y':
        input('Throw cubic...')
        cubic1 = random.randint(1,7)
        cubic2 = random.randint(1,7)
        sum = cubic1 + cubic2
        if sum == 7:
            message = f'{cubic1} + {cubic2} = {sum}, You win.'
            money += 5
        else:
            message = f'{cubic1} + {cubic2} != {sum}, You lose.'
            money -= 1
        print(message)
        print(f'Your money is {money} baht.')
        move_on = input('Continue... (y/n)')


def min_max():
    min = max = 0
    for x in range(4):
        num1 = input(f'รับค่า ตัวเลข {x+1}>> ')
        
lucky_seven()
