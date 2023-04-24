import telebot
from math import sqrt
from datetime import datetime
from random import randint, choice

bot = telebot.TeleBot("6201499506:AAGkJeT6ahdVPbrFcRjcilaJNCjzqThnYU4")


@bot.message_handler(commands=['start'])
def handle_percent(message):
    bot.reply_to(message, """
Привет!
Я бот-помощник, который может помочь с некоторыми задачами
Чтобы узнать мой функционал, введите /help""")


@bot.message_handler(commands=['help'])
def help(message):
    parts = message.text.split(' ')
    if len(parts) == 1:
        bot.reply_to(message, """
На данный момент досутпны следующие команды:
/percent - нахождение процента от числа
/reduce - сокращение дроби
/vectors_sum - нахождение сумм 2-х и более векторов по их координатам
/vectors_sub - нахождение разницы 2-х по их координатам
/middle_of_segm - нахождение координат середины отрезка по координатам его концов
/length_of_segm - нахождение длины середины отрезка по координатам его концов
/date - выводит дату и время
/rand_num - выбирает рандомное число
/random - выводит рандомно одно слово из тех, что вы предали
Если вы используете команду в первый раз, рекомендуем подробнее узнать о команде,
прописав help <название команды>, например help percent
Если же вы хотите узнать как работает команда, рекомендуем подробнее узнать о команде,
прописав info <название команды>, например info percent""")
    elif len(parts) == 2 and parts[1].lower() == "percent":
        bot.reply_to(message, """
Чтобы команда правильно заработала 
после команды нужно ввести, число, от которого хочешь получить проценты,
и затем сами проценты,
например /percent 100 15
Эта команда выведет 15 процентов от 100, то-есть 15""")
    elif len(parts) == 2 and parts[1].lower() == "reduce":
        bot.reply_to(message, """
Чтобы команда правильно заработала 
после команды нужно ввести числитель и знаменатель дроби,
например /reduce 10 25
Эта команда выведет сокращеную дробь 10/25, то есть 2/5""")
    elif len(parts) == 2 and parts[1].lower() == "vectors_sum":
        bot.reply_to(message, """
Чтобы команда правильно заработала 
после команды нужно ввести координаты первого вектора,
а затем координаты второго вектора
например /vectors_sum 3 5 7 -1
Эта команда выведет сумму векторов (3;5) и (7;-1),
то-есть вектор (10;4)""")
    elif len(parts) == 2 and parts[1].lower() == "vectors_sub":
        bot.reply_to(message, """
Чтобы команда правильно заработала 
после команды нужно ввести координаты вектора, из которого будут вычитать
а затем координаты вычитаемого вектора
например /vectors_sum 3 5 7 -1
Эта команда выведет разницу векторов (3;5) и (7;-1),
то-есть вектор (4;-6)""")
    elif len(parts) == 2 and parts[1].lower() == "middle_of_segm":
        bot.reply_to(message, """
Чтобы команда правильно заработала 
после команды нужно ввести координаты концов отрезка
например /middle_of_segm 1 1 5 5
Эта команда выведет середину отрезка (1;1) (5;5),
то-есть точка (3;3)""")
    elif len(parts) == 2 and parts[1].lower() == "length_of_segm":
        bot.reply_to(message, """
Чтобы команда правильно заработала 
после команды нужно ввести координаты концов отрезка
например /length_of_segm 1 1 5 5
Эта команда выведет длину отрезка (1;1) (5;5),
то-есть 5,657""")
    elif len(parts) == 2 and parts[1].lower() == "help":
        bot.reply_to(message, """
Просто введите /help, чтобы посмотреть доступные команды
Чтобы узнать, как работает команда, напишите /help <название команды>""")
    elif len(parts) == 2 and parts[1].lower() == "info":
        bot.reply_to(message, """
Просто введите /info, чтобы узнать, как работает команда,
напишите /info <название команды>""")
    elif len(parts) == 2 and parts[1].lower() == "rand_num":
        bot.reply_to(message, """
Если просто ввести команду, то она рандомно выдаст число от 1 до 100
Но можно написать два числа, первое меньше второго, и тогда она выдаст рандомное число в этом промежутке """)
    elif len(parts) == 2 and parts[1].lower() == "random":
        bot.reply_to(message, """
Напишите команду и после неё через пробел слова или что-то ещё,
 из чего надо что-то рандомно выбрать
        """)
    elif len(parts) == 2 and parts[1].lower() == "":
        bot.reply_to(message, """
        """)
    elif len(parts) == 2 and parts[1].lower() == "":
        bot.reply_to(message, """
        """)


@bot.message_handler(commands=['info'])
def info(message):
    parts = message.text.split(' ')
    if len(parts) == 1:
        bot.reply_to(message, """Эта команда может рассказать, как работают некоторые команды этого бота
Чтобы узнать, как работают команды, пропишите /info <назваие команды>""")
    elif len(parts) == 2 and parts[1].lower() in "percent":
        bot.reply_to(message, """
Чтобы найти процент от числа надо это 
число умножить на процент и поделить на 100
Таким образом, при команде
/percent 100 15
Получается 15""")
    elif len(parts) == 2 and parts[1].lower() == "reduce":
        bot.reply_to(message, """
Эта команда использует алгоритм Евклида для нахождения
наибольшего общего делителя числителя и знаменателя,
после чего делит оба числа на этот делитель,
а вы думайте сами
Таким образом, при команде
/reduce 10 25
получается 15""")
    elif len(parts) == 2 and parts[1].lower() == "vectors_sum":
        bot.reply_to(message, """
Сумма векторов находится суммой их координат
{x1;y1} + {x2;y2} -> {x1+x2;y1+y2}
Таким образом, при команде
/vectors_sum 3 5 7 -1
получается вектор (10;4)""")
    elif len(parts) == 2 and parts[1].lower() == "vectors_sub":
        bot.reply_to(message, """
Разница векторов находится разницей координаты второго вектора из первого
{x1;y1} + {x2;y2} -> {x2-x1;y2-y1}
Таким образом, при команде
/vectors_sub 3 5 7 -1
получается вектор (4;-6)""")
    elif len(parts) == 2 and parts[1].lower() == "middle_of_segm":
        bot.reply_to(message, """
Середина отрезка по координатам находится разницей каждой из координат, делёной пополам
(x1;y1);(x2;y2) -> ((x1+x2)/2;(y1+y2)/2)
Таким образом, при команде 
/middle_of_segm 1 1 5 5
получается точка (3;3)""")
    elif len(parts) == 2 and parts[1].lower() == "length_of_segm":
        bot.reply_to(message, """
Длина отрезка по координатам находится квадратным корнем квадратов разниц координат
(x1;y1);(x2;y2) -> квадратный корень из (x2-x1)^2+(y2-y1)^2
Таким образом, при команде /middle_of_segm 1 1 5 5
получается примерно 5,657)""")
    elif len(parts) == 2 and parts[1].lower() == "help":
        bot.reply_to(message, """Эта команда подсказывает, как правильно использовать команды""")
    elif len(parts) == 2 and parts[1].lower() == "info":
        bot.reply_to(message, """Эта команда рассказывает, как работают некоторые команды""")
    elif len(parts) == 2 and parts[1].lower() == "rand_num":
        bot.reply_to(message, """
Так и работает, выбирает рандомное числов промежутке
            """)
    elif len(parts) == 2 and parts[1].lower() == "random":
        bot.reply_to(message, """
Так и работает, выбирает рандомное слово и написанных вами
            """)
    elif len(parts) == 2 and parts[1].lower() == "":
        bot.reply_to(message, """
            """)
    elif len(parts) == 2 and parts[1].lower() == "":
        bot.reply_to(message, """
            """)
    elif len(parts) == 2 and parts[1].lower() == "":
        pass


@bot.message_handler(commands=['percent'])
def handle_percent(message):
    try:
        parts = message.text.split(' ')
        if len(parts) != 3:
            raise ValueError()
        number = float(parts[1])
        percent = float(parts[2])
        result = number * percent / 100
        bot.reply_to(message, f"{percent}% от {number} = {result}")
    except ValueError:
        bot.reply_to(message, """
Некорректный запрос 
Пример:
/percent 100 15""")


@bot.message_handler(commands=['reduce'])
def handle_reduce(message):
    try:
        parts = message.text.split(' ')
        if len(parts) != 3:
            raise ValueError()
        numerator = int(parts[1])
        denominator = int(parts[2])
        for factor in range(2, min(numerator, denominator) + 1):
            while numerator % factor == 0 and denominator % factor == 0:
                numerator //= factor
                denominator //= factor
        bot.reply_to(message, f"{parts[1]}/{parts[2]} = {numerator}/{denominator}")
    except ValueError:
        bot.reply_to(message, """
Некорректный запрос
Пример:
/reduce 10 25""")


@bot.message_handler(commands=['vectors_sum'])
def vectors_sum(message):
    try:
        parts = message.text.split(' ')
        if len(parts) < 5:
            print('ERROR')
            raise ValueError()
        elif len(parts) == 5:
            x1 = float(parts[1])
            y1 = float(parts[2])
            x2 = float(parts[3])
            y2 = float(parts[4])
            result = f"({x1 + x2}; {y1 + y2})"
            bot.reply_to(message, f"Сумма векторов ({x1};{y1}) и ({x2};{y2}) вектор {result}")
        elif len(parts) % 2 == 1:
            x1 = 0
            y1 = 0
            for i in parts[1::2]:
                x1 += float(i)
                y1 += float(parts[parts.index(i) + 1])
            bot.reply_to(message, f"Суммой всех векторов являетя вектор ({x1};{y1})")
    except ValueError:
        bot.reply_to(message, """
Некорректный запрос
Пример:
/vectors_sum 3 5 7 -1""")


@bot.message_handler(commands=['vectors_sub'])
def vectors_sub(message):
    try:
        parts = message.text.split(' ')
        if len(parts) != 5:
            print('ERROR')
            raise ValueError()
        elif len(parts) == 5:
            x1 = float(parts[1])
            y1 = float(parts[2])
            x2 = float(parts[3])
            y2 = float(parts[4])
            result = f"({x2 - x1}; {y2 - y1})"
            bot.reply_to(message, f"Разница векторов ({x1};{y1}) и ({x2};{y2}) вектор {result}")
    except ValueError:
        bot.reply_to(message, """
Некорректный запрос
Пример:
/vectors_sum 3 5 7 -1""")


@bot.message_handler(commands=['middle_of_segm'])
def middle_of_segm(message):
    try:
        parts = message.text.split(' ')
        if len(parts) != 5:
            print('ERROR')
            raise ValueError()
        elif len(parts) == 5:
            x1 = float(parts[1])
            y1 = float(parts[2])
            x2 = float(parts[3])
            y2 = float(parts[4])
            result = f"({(x2 - x1) / 2}; {(y2 - y1) / 2})"
            bot.reply_to(message, f"Середина отрезка ({x1};{y1})-({x2};{y2}) точка {result}")
            bot.reply_to(message, f"")
    except ValueError:
        bot.reply_to(message, """
Некорректный запрос
Пример:
/middle_of_segm 1 1 5 5
""")


@bot.message_handler(commands=['length_of_segm'])
def length_of_segm(message):
    try:
        parts = message.text.split(' ')
        if len(parts) != 5:
            print('ERROR')
            raise ValueError()
        elif len(parts) == 5:
            x1 = float(parts[1])
            y1 = float(parts[2])
            x2 = float(parts[3])
            y2 = float(parts[4])
            result = f"{round(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 3)}"
            bot.reply_to(message, f"Длина отрезка ({x1};{y1})-({x2};{y2}) равна {result}")
    except ValueError:
        bot.reply_to(message, """
Некорректный запрос
Пример:
/length_of_segm 1 1 5 5
""")


@bot.message_handler(commands=['date'])
def date(message):
    bot.reply_to(message, f"""{datetime.now()}""")


@bot.message_handler(commands=['rand_num'])
def rand_num(message):
    try:
        parts = message.text.split(' ')
        if len(parts) == 1:
            bot.reply_to(message, f"""{randint(1, 100)}""")
        elif len(parts) == 3:
            if int(parts[1]) < int(parts[1]):
                print('ERROR')
                raise ValueError()
            bot.reply_to(message, f"""{randint(int(parts[1]), int(parts[2]))}""")
    except ValueError:
        bot.reply_to(message, """
Некорректный запрос
Пример:
/rand_num 1 5
/rand_num
""")


@bot.message_handler(commands=['random'])
def rand_num(message):
    try:
        parts = message.text.split(' ')
        if len(parts) == 1:
            raise ValueError
        elif len(parts) > 1:
            bot.reply_to(message, f"""{choice(parts[1:])}""")
    except ValueError:
        bot.reply_to(message, """
Некорректный запрос 
Пример:
/random 100 15""")


bot.polling()
# "6201499506:AAGkJeT6ahdVPbrFcRjcilaJNCjzqThnYU4"
