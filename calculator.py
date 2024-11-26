to_num = {
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
    "тысяча": 1000,
}

to_words = {value: key for key, value in to_num.items()}

operations = {
    "плюс": "+",
    "минус": "-",
    "умножить": "*",
}


def main():
    """Запрашивает у пользователя математические выражения, записанные словами.
    Программа запрашивает математические выражения, пока пользователь на введёт "выход"

    Raises:
        ValueError: 1) число меньше нуля или больше ста
            2) слово не является ни числом, ни математической операцией
        TypeError: возникает при неправильном чередовании чисел и операций

    Side effects:
        выводит на экран результат вычислений в словесной форме
    """
    print(
        """Добро пожаловать в калькулятор! 
Введите <число> <операция> <число> в формате "двадцать пять плюс тринадцать один". 
Вводите только числа от 0 до 100. Из операций доступны только "плюс", "минус", "умножить"
Введите "выход", чтобы выйти из программы """
    )

    while True:
        string = input("Выражение: ").lower().strip()
        if string == "выход":
            break

        try:
            print(translate_number(eval(translate_words(string))))
        except ValueError as err1:
            print(err1)
        except TypeError:
            print("Неправильная запись операций!")
        except:
            pass


def translate_words(string):
    """Переводит выражение, записанное словами, в математическую форму

    Args:
        string (str): математическое выражение, записанное словами

    Returns:
        str: выражение, записанное в виде цифр и знаков

    Examples:
        translate_words("двадцать пять плюс тринадцать") -> "25 + 13"
        translate_words("пять плюс два умножить три минус один") -> "5 + 2 * 3 - 1"

    Raises:
        ValueError: 1) число меньше нуля или больше ста
            2) слово не является ни числом, ни математической операцией
        TypeError: возникает при неправильном чередовании чисел и операций
    """
    words = string.split()
    expression = []
    num = None

    for word in words:
        if word in to_num:
            num = to_num[word] if num == None else num + to_num[word]
        elif word in operations and check_num(num):
            expression.extend([str(num), operations[word]])
            num = None
        else:
            raise ValueError(f'Незнакомое слово "{word}"!')

    if check_num(num):
        expression.append(str(num))

    return " ".join(expression)


def check_num(num):
    if (0 <= num <= 100) == False:
        raise ValueError("Все числа должны быть от 0 до 100!")
    return True


def translate_number(num):
    """Переводит число в словесную форму

    Args:
        num (int): число

    Returns:
        str: словесную форму числа

    Examples:
        translate_number(16) -> шестнадцать
        translate_number(-105) -> минус сто пять
        translate_number(2) -> два
    """
    result = []
    if num < 0:
        result.append("минус")
        num = -num

    for pos in range(len(str(num)) - 1, -1, -1):
        if 11 <= num <= 19:
            result.append(to_words[num])
            break
        else:
            dig = num - num % 10**pos
            num -= dig
            if dig == 0 and len(result) != 0:
                continue
            result.append(to_words[dig])

    return " ".join(result)


main()
