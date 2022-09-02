name_list = []
word_list = []

name = None


def player_name():
    while True:
        name = input('Введіть імя')
        if name == 'Start':
            break
        else:
            name_list.append(name)


def func():
    while True:
        for i in name_list:
            slovo = input(f'{i}, введи будь ласка слово')
            while slovo in word_list:
                if slovo in word_list:
                    print('це слово вже використовувалось, введіть інше')
                    slovo = input(f'{i}, введи будь ласка слово')
                else:
                    word_list.append(slovo)
                    break

            word_list.append(slovo)


player_name()
func()
print(name_list, word_list)
