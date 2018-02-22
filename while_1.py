user_name = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
while True:
    user_name.pop()
    print(user_name)

    if "Валера" in user_name:
        print("Валера нашелся")
    break
