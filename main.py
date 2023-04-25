import telebot  # импортируем телебот
from math import sqrt  # импортируем извлечение из-под корня
from datetime import datetime  # импортируем время
from random import randint, choice  # импортируем, что-надо

# подключаем бота по токену
bot = telebot.TeleBot("6201499506:AAGkJeT6ahdVPbrFcRjcilaJNCjzqThnYU4")
# списки для функции перевода(conversion)
conv1 = ['мм', 'см', 'дм', 'м']
conv2 = ['мм2', 'см2', 'дм2', 'м2']
conv3 = ['мм3', 'см3', 'дм3 ', 'м3']
conv4 = ['мс', 'кмч', 'м/с', 'км/ч']
conv5 = ['с', 'мин', 'ч', 'сут']


# Старт
@bot.message_handler(commands=['start'])
def handle_percent(message):
    bot.reply_to(message, """
Привет!
Я бот-помощник, который может помочь с некоторыми задачами
Чтобы узнать мой функционал, введите /help""")


# хелп общий и для функций бота
@bot.message_handler(commands=['help'])
def help(message):
    parts = message.text.split(' ')
    if len(parts) == 1:
        bot.reply_to(message, """
На данный момент доступны следующие команды:
/percent - нахождение процента от числа
/reduce - сокращение дроби
/vectors_sum - нахождение сумм 2-х и более векторов по их координатам
/vectors_sub - нахождение разницы 2-х векторов по их координатам
/middle_of_segm - нахождение координат середины отрезка по координатам его концов
/length_of_segm - нахождение длины отрезка по координатам его концов
/date - выводит дату и время
/rand_num - выбирает рандомное число
/random - выводит рандомно одно слово из тех, что вы передали
/conversion - перевод некоторых единиц
Если вы используете команду в первый раз, рекомендуем подробнее узнать о команде,
прописав /help <название команды>, например /help something
Если же вы хотите узнать как работает команда, рекомендуем подробнее узнать о команде,
прописав /info <название команды>, например /info something""")
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
    elif len(parts) == 2 and parts[1].lower() == "something":
        bot.reply_to(message, """
Что-то""")
    elif len(parts) == 2 and parts[1].lower() == "conversion":
        bot.reply_to(message, """
Сначала нужно ввести число, которое надо будет перевести,
затем из чего переводим и во что переводим
команда работает только с величинами длины, площади и объёма от миллиметров до метров,
скорости метры в секунду и километры в час,
а также временем от секунд до суток
Чтобы посмотреть сокращения:
/help conversion_list""")
    elif len(parts) == 2 and parts[1].lower() == "conversion_list":
        bot.reply_to(message, """
Сокращения:
мм - миллиметры
см - сантиметры
дм - дециметры
м - метры
Чтобы переводить площади приписывайте после обозначений сверху двойку(м2)
Чтобы переводить объёмы приписывайте после обозначений сверху тройку(м3)
м/с(мс) - метры в секунду
км/ч(кмч) - километры в час
с - секунды
мин - минуты
ч - часы
сут - сутки""")


# инфо общее и для отдельных команд
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
Таким образом, при команде /length_of_segm 1 1 5 5
получается примерно 5,657)
Подробнее здесь: https://ru.wikihow.com/вычислить-длину-отрезка-по-координатам""")
    elif len(parts) == 2 and parts[1].lower() == "help":
        bot.reply_to(message, """Эта команда подсказывает, как правильно использовать команды""")
    elif len(parts) == 2 and parts[1].lower() == "info":
        bot.reply_to(message, """Эта команда рассказывает, как работают некоторые команды""")
    elif len(parts) == 2 and parts[1].lower() == "rand_num":
        bot.reply_to(message, """
Так и работает, выбирает рандомное числов промежутке""")
    elif len(parts) == 2 and parts[1].lower() == "random":
        bot.reply_to(message, """
Так и работает, выбирает рандомное слово и написанных вами""")
    elif len(parts) == 2 and parts[1].lower() == "something":
        bot.reply_to(message, """
Что-то""")
    elif len(parts) == 2 and parts[1].lower() == "conversion":
        bot.reply_to(message, """
Предлагаем ознакомиться с материалом:
https://intmag24.ru/dlya-shkolnikov/perevod-edinits-izmereniya/
            """)


# команда получения процента от числа
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


# команда сокращения дроби
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


# команда сложения векторов по их координатам
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


# команда вычитания векторов по их координатам
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


# команда нахождения середина отрезка по координатам концов
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


# команда нахождения длины отрезка по координатам его концов
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


# просто команда, выводящая время
@bot.message_handler(commands=['date'])
def date(message):
    bot.reply_to(message, f"""{datetime.now()}""")


# команда вывода рандомного числа
@bot.message_handler(commands=['rand_num'])
def rand_num(message):
    try:
        parts = message.text.split(' ')
        if len(parts) == 1:
            bot.reply_to(message, f"""{randint(1, 100)}""")
        elif len(parts) == 3:
            if int(parts[1]) < int(parts[1]):
                raise ValueError()
            bot.reply_to(message, f"""{randint(int(parts[1]), int(parts[2]))}""")
    except ValueError:
        bot.reply_to(message, """
Некорректный запрос
Пример:
/rand_num 1 5
/rand_num
""")


# команда вывода рандомного из написанного
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


# функция перевода длин
def convers1(num, fromm, to):
    return round((10 ** (conv1.index(fromm) - conv1.index(to))) * num, 3)


# функция перевода площадей
def convers2(num, fromm, to):
    return round((100 ** (conv2.index(fromm) - conv2.index(to))) * num, 3)


# функция перевода объёмов
def convers3(num, fromm, to):
    return round((1000 ** (conv3.index(fromm) - conv3.index(to))) * num, 3)


# функция перевода скорости
def convers4(num, fromm, to):
    if fromm == to:
        return num
    elif fromm in ['мс', 'м/с']:
        return num * 3.6
    else:
        return round(num / 3.6, 5)


# функция перевода времени
def convers5(num, fromm, to):
    count = conv5.index(fromm) - conv5.index(to)
    if count == 3:
        return num * 24 * 60 * 60
    elif count == 2 and fromm == 'сут':
        return num * 24 * 60
    elif count == 2 and fromm != 'сут':
        return num * 60 * 60
    elif count == 1 and fromm == 'сут':
        return num * 24
    elif count == 1 and fromm != 'сут':
        return num * 60
    elif count == 0:
        return num
    elif count == -1 and to == 'сут':
        return round(num / 24, 3)
    elif count == -1 and to != 'сут':
        return round(num / 60, 3)
    elif count == -2 and to == 'сут':
        return round(num / (60 * 24), 3)
    elif count == -2 and to != 'сут':
        return round(num / (60 * 60), 3)
    elif count == -3 and to == 'сут':
        return round(num / (60 * 60 * 24), 3)


#  сама команда перевода различных величин
@bot.message_handler(commands=['conversion'])
def conversion(message):
    try:
        parts = message.text.split(' ')
        if len(parts) != 4:
            raise ValueError
        else:
            if parts[2].lower() in conv1 and parts[3].lower() in conv1:
                bot.reply_to(message, f"""
{convers1(float(parts[1]), parts[2], parts[3])} {parts[3]}""")
            elif parts[2].lower() in conv2 and parts[3].lower() in conv2:
                bot.reply_to(message, f"""
{convers2(float(parts[1]), parts[2], parts[3])} {parts[3]}""")
            elif parts[2].lower() in conv3 and parts[3].lower() in conv3:
                bot.reply_to(message, f"""
{convers3(float(parts[1]), parts[2], parts[3])} {parts[3]}""")
            elif parts[2].lower() in conv4 and parts[3].lower() in conv4:
                bot.reply_to(message, f"""
{convers4(float(parts[1]), parts[2], parts[3])} {parts[3]}""")
            elif parts[2].lower() in conv5 and parts[3].lower() in conv5:
                bot.reply_to(message, f"""
{convers5(float(parts[1]), parts[2], parts[3])} {parts[3]}""")
            else:
                raise ValueError
    except ValueError:
        bot.reply_to(message, """
Некорректный запрос 
Пример:
/conversion 100 см м""")


# фишечки
@bot.message_handler(commands=['666'])
def rand_num(message):
    bot.reply_to(message, f"""
Satano! Oro te appare te rosto!
Veni, Satano! Ter oro te!
Veni, Satano! Oro te pro arte!
Veni, Satano! Opera pra estro, Ater oro!
Veni, Satano! Oro te! Appare te rosto!
Veni, Satano! Amen.""")


# фишечки
@bot.message_handler(commands=['777'])
def rand_num(message):
    bot.reply_to(message, f"""
У нас здесь не Лас-Вегас""")


# @bot.message_handler(commands=['god?'])
# def rand_num(message):
# bot.reply_to(message, f"""
# Дядя Дима, поставьте 100 баллов""")

# запуск бота
bot.polling()
# "6201499506:AAGkJeT6ahdVPbrFcRjcilaJNCjzqThnYU4"
# ^ токен
