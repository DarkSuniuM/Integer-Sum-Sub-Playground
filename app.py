from random import randint, choice

print("Type \"exit\" to Exit the program.")
OPERATORS = ('-', '+')
HAPPY_ANSWERS = ('Good job',
                 'Nice',
                 'That\'s what I\'m talking about',
                 'Yeah Baby')
SAD_ANSWERS = ('Oh nooo',
               'It\'s wrong',
               'You can do better',
               'Be more careful')


def getAnswer(first_operand: int, second_operand: int, operator: str):
    if operator == '+':
        return first_operand + second_operand
    if operator == '-':
        return first_operand - second_operand


def checkAnswer(expected_answer, given_answer):
    return int(expected_answer) == int(given_answer)


while True:
    operator = choice(OPERATORS)
    first_operand = randint(-50, +50)
    second_operand = randint(-50, +50)
    user_answer = input(f"{first_operand} {operator} {second_operand} = ")
    while not user_answer.isdecimal() and user_answer != 'exit':
        print("The answer should be a decimal/integer number!")
        user_answer = input(f"{first_operand} {operator} {second_operand} = ")
    if user_answer == "exit":
        break
    real_answer = getAnswer(first_operand, second_operand, operator)
    if checkAnswer(real_answer, user_answer):
        print(choice(HAPPY_ANSWERS))
        continue
    print(choice(SAD_ANSWERS),
          f", The answer was {real_answer}. :(")
