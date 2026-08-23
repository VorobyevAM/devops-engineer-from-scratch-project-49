import random

DESCRIPTION = 'What is the result of the expression?'

OPERATIONS = ('+', '-', '*')


def calculate(number1, number2, operation):
    match operation:
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case '*':
            return number1 * number2


def generate_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operation = random.choice(OPERATIONS)

    question = f'{number1} {operation} {number2}'
    correct_answer = str(calculate(number1, number2, operation))

    return question, correct_answer