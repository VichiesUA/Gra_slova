name_list = []
word_list = []
res = {}

print('''----------------------------
Вас вітає гра в "слова"
Для початку введіть імена гравців. 
Напишіть "start" для початку гри.
----------------------------''')


def player_name():
    while True:
        name = input('Введіть і\'мя: \n')
        if name == 'start':
            break

        name_list.append(name.upper())
        res.setdefault(name.upper(), 0)


def word():
    while True:
        for i in name_list:
            if len(word_list) == 0:
                slovo = input(f'{i}, введіть слово: \n').lower()
                word_list.append(slovo)
                res[i] += 1
            else:
                last_word = str(word_list[-1])
                slovo = input(f'{i}, введіть слово на букву "{last_word[-1]}": \n').lower()
                if slovo == 'stop':
                    for key, value in res.items():
                        print(f' {key} ввів стільки слів ==> {value}')
                    print('-------------------------------')
                    print(f'Всього слів ==> {len(word_list)}')
                    exit()
                else:
                    while True:
                        if slovo == 'stop':
                            for key, value in res.items():
                                print(f' {key} ввів стільки слів ==> {value}')
                            print('-------------------------------')
                            print(f'Всього слів ==> {len(word_list)}')
                            exit()
                        elif not slovo.startswith(last_word[-1]):
                            print('Це слово починається з іншої букви!')
                            slovo = input(f'{i}, введіть слово на букву "{last_word[-1]}": \n').lower()
                        elif slovo in word_list:
                            print('Це слово вже використовувалось, введіть інше: \n')
                            slovo = input(f'{i}, введіть слово на букву "{last_word[-1]}": \n').lower()
                        else:
                            word_list.append(slovo)
                            res[i] += 1
                            break


player_name()
print('''--------------------------------
Гра розпочалась! Щоб закінчити гру напишіть "stop".
--------------------------------''')
word()
