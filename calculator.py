words_to_num = {
    "ноль": 0,
    "один": 1,
    "два": 2,
    "три": 3,
    "четыре": 4,
    "пять": 5,
    "шесть": 6,
    "семь": 7,
    "восемь": 8,
    "девять": 9,
    "десять": 10,
    "одиннадцать": 11,
    "двенадцать": 12,
    "тринадцать": 13,
    "четырнадцать": 14,
    "пятнадцать": 15,
    "шестнадцать": 16,
    "семнадцать": 17,
    "восемнадцать": 18,
    "девятнадцать": 19,
    "двадцать": 20,
    "тридцать": 30,
    "сорок": 40,
    "пятьдесят": 50,
    "шестьдесят": 60,
    "семьдесят": 70,
    "восемьдесят": 80,
    "девяносто": 90,
    "сто": 100,
    "двести": 200,
    "триста": 300,
    "четыреста": 400,
    "пятьсот": 500,
    "шестьсот": 600,
    "семьсот": 700,
    "восемьсот": 800,
    "девятьсот": 900,
    "одна тысяча": 1000,
    "две тысячи": 2000,
    "три тысячи": 3000,
    "четыре тысячи": 4000,
    "пять тысяч": 5000,
    "шесть тысяч": 6000,
    "семь тысяч": 7000,
    "восемь тысяч": 8000,
    "девять тысяч": 9000,
}

num_to_words = {value: key for key, value in words_to_num.items()}

operations = {
    "плюс": "+",
    "минус": "-",
    "умножить": "*",
}


def main():
    print(
        '''Добро пожаловать в калькулятор! \nВведите <число> <операция> <число> в формате "двадцать пять плюс тринадцать один". \nВводите только числа от 0 до 100. Из операций доступны только "плюс", "минус", "умножить"'''
    )
    expression = calculate(translate_words())
    print(translate_number(expression))


def calculate(expr):
    return perform_operation(expr[0], expr[1], expr[2])


def perform_operation(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    return num1 * num2


def translate_words():
    words = input().split()
    expression = []
    num = None

    for word in words:
        if word in words_to_num:
            num = words_to_num[word] if num == None else num + words_to_num[word]
        elif word in operations:
            expression.extend([num, operations[word]])
            num = None
        else:
            print(f"""Неккоректный ввод в слове {word}!""")
            translate_words()

    if num != None:
        expression.append(num)

    return expression


def translate_number(num):
    result = []
    if num < 0:
        result.append("минус")
        num = -num

    for i in range(len(str(num)) - 1, -1, -1):
        dig = None
        if 11 <= num <= 19:
            result.append(num_to_words[num])
            break
        else:
            dig = num - num % 10**i
            num -= dig

        if dig != None:
            result.append(num_to_words[dig])

    return " ".join(result)


main()