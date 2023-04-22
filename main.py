import telebot

bot = telebot.TeleBot("6201499506:AAGkJeT6ahdVPbrFcRjcilaJNCjzqThnYU4")


@bot.message_handler(commands=['start'])
def handle_percent(message):
    bot.reply_to(message, """Привет!
Я бот-помощник, который может помочь с некоторыми задачами
Чтобы узнать мой функционал, введите /help""")


@bot.message_handler(commands=['help'])
def handle_percent(message):
    bot.reply_to(message, """На данный момент досутпны следующие команды:
/percent - нахождение процента от числа
/reduce - сокращение дроби
/vectors_sum - нахождение сумм 2-х и более векторов по их координатам
Если вы используете команду в первый раз, рекомендуем подробнее узнать о команде,
прописав <название команды>_help, например percent_help
Если же вы хотите узнать как работает команда, рекомендуем подробнее узнать о команде,
прописав <название команды>_info, например percent_info""")


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
        bot.reply_to(message, """Некорректный запрос. Пример:
/percent 100 15
/percent_help""")


@bot.message_handler(commands=['percent_help'])
def handle_percent_help(message):
    bot.reply_to(message, """
Чтобы команда правильно заработала 
после команды нужно ввести, число, от которого хочешь получить проценты,
и затем сами проценты,
например /percent 100 15
Эта команда выведет 15 процентов от 100, то-есть 15""")


@bot.message_handler(commands=['percent_info'])
def handle_percent_info(message):
    bot.reply_to(message, """
Команда берёт число, от которого надо найти процент,
умножает его на этот процент и 
делит получившееся число на 100
Таким образом, при команде /percent 100 15, умножает 15 на 100 и делит на 100
Получается 15""")


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
        bot.reply_to(message, """Некорректный запрос. Пример:
/reduce 10 25
/reduce_help""")


@bot.message_handler(commands=['reduce_help'])
def handle_reduce_help(message):
    bot.reply_to(message, """
Чтобы команда правильно заработала 
после команды нужно ввести числитель и знаменатель дроби,
например /reduce 10 25
Эта команда выведет сокращеную дробь 10/25, то есть 2/5""")


@bot.message_handler(commands=['reduce_info'])
def handle_reduce_info(message):
    bot.reply_to(message, """
Эта команда использует алгоритм Евклида для нахождения
наибольшего общего делителя числителя и знаменателя,
после чего делит оба числа на этот делитель
Таким образом, при команде /reduce 10 25
получается 15""")


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
                y1 += float(parts[parts.index(i) + 2])
            bot.reply_to(message, f"Суммой всех векторов являетя вектор ({x1};{y1})")
    except ValueError:
        bot.reply_to(message, """Некорректный запрос. Пример:
/vectors_sum 3 5 7 -1
/vectors_sum_help""")


@bot.message_handler(commands=['vectors_sum_help'])
def vectors_sum_help(message):
    bot.reply_to(message, """
Чтобы команда правильно заработала 
после команды нужно ввести координаты первого вектора,
а затем координаты второго вектора
например /vectors_sum 3 5 7 -1
Эта команда выведет сумму векторов (3;5) и (7;-1),
то-есть вектор (8;6)""")


@bot.message_handler(commands=['vectors_sum_info'])
def vectors_sum_info(message):
    bot.reply_to(message, """
Сумма векторов нахидится суммой их координат
Команда складывает x-координаты и y-координаты 2-х векторов
Полученные суммы являются x-координатой и y-координатой двух сложенных векторов
Таким образом, при команде /vectors_sum 3 5 7 -1
получается вектор (8;6)""")

bot.polling()
# "6201499506:AAGkJeT6ahdVPbrFcRjcilaJNCjzqThnYU4"
