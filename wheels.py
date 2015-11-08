from datetime import date
import datetime
import random
import re

wheels = ["ruota di Bari", "ruota di Cagliari", "ruota di Firenze",
"ruota di Genova", "ruota di Milano", "ruota di Napoli",
"ruota di Palermo", "ruota di Roma", "ruota di Torino",
"ruota di Venezia", "ruota Nazionale"]

def getseed(wheel) :
    today = date.today()
    #today = datetime.date(2015, 10, 30)
    year = today.year
    weekofyear = today.isocalendar()[1]
    weekday = today.weekday()
    seedday = 3
    if weekday == 6 or weekday == 0 or weekday == 1:
        seedday = 1
        if weekday == 6:
            weekofyear = weekofyear + 1
    elif weekday == 2 or weekday == 3:
        seedday = 2
    seed = wheel.upper() + "-" + str(year) + "-" + str(weekofyear) + "-" + str(seedday)
    return seed;

def getnumbers(wheel, n):
    numbers = None
    if wheel.upper() in (w.upper() for w in wheels):
        seed = getseed(wheel)
        random.seed(seed)
        numbers = getrandomsubsetofnumbers(n)
    return numbers

def getfirstwheelfound(text):
    for w in wheels:
        if (w.upper() in text.upper()):
            return w
    return ""

def getnumberstoplay(text):
    if re.search('ambo', text, re.IGNORECASE):
        return 2
    if re.search('terno', text, re.IGNORECASE):
        return 3
    if re.search('quaterna', text, re.IGNORECASE):
        return 4
    if re.search('terna', text, re.IGNORECASE):
        return 3
    return 5

def gettextforkindofplay(n):
    if (n == 2):
        return " per un ambo "
    if (n == 3):
        return " per un terno "
    if (n == 4):
        return " per una quaterna "
    return " "

def getrandomsubsetofnumbers(n):
    count = 0;
    numbers = []
    while count != n:
        current = random.randint(1, 90)
        if current not in numbers:
            numbers.append(current)
            count = count + 1
    numbers.sort()
    return numbers

print gettextforkindofplay(5)
