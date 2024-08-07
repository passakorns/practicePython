def coffeeMenu():
    total = 0
    while True:
        print('!!=== Coffee Menu ===!!!')
        print('1. Americano 50')
        print('2. Late 60')
        print('3. Cappuccino 60')
        select = input('Select item 1-3 or not to exit>> ')
        if select == '1':
            print('Americano...')
            total += 50
        elif select == '2':
            print('Late....')
            total += 60
        elif select == '3':
            print('Cappuccino')
            total += 60
        else:
            break
    print('...Bye Close Shop...')
    print(f'Total income {total:,.2f} bath')
coffeeMenu()