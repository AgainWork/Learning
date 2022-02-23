try:
    text = input('Введите что-нибудь -->')
except E0FError:
    print('Ну зачем вы сделали мне E0F?')
except KeyboardInterrupt:
    print('Вы отменили операцию.')
else:
    print('Вы ввели {0}'.format(text))