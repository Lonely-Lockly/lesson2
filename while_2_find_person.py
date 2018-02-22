user_name = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']

while True:
    try:
        find_person = input('name ')
        if find_person in user_name:
            print(find_person)
            break
        else:
            print("Попробуй другое имя!")
    except EOFError:
        print("произошла ошибка")