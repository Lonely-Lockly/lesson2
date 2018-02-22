answers = {
    'привет': 'Привет!',
    'как дела': 'Лучше всех!',
    'пока': 'Увидимся!'
}

def get_answer(question, answers):
    return answers.get(question)

def ask_user(answers):
    while True:
        try:
            user_input = input("Скажи что-нибудь: ")
            answer = get_answer(user_input, answers)
            print(answer)

            if user_input == 'пока':
                break
        except (SyntaxError, KeyError, TypeError, ValueError, KeyboardInterrupt):
            print("Жаль, что Вы уже уходите!")
ask_user(answers)