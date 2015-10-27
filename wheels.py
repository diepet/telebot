from datetime import date
import datetime
import random

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

def getnumbers(wheel):
    numbers = []
    if wheel.upper() in (w.upper() for w in wheels):
        seed = getseed(wheel)
        random.seed(seed)
        numbers.append(random.randint(1, 90))
        numbers.append(random.randint(1, 90))
        numbers.append(random.randint(1, 90))
        numbers.append(random.randint(1, 90))
        numbers.append(random.randint(1, 90))
        numbers.sort()
    return numbers

def getfirstwheelfound(text):
    for w in wheels:
        if (w.upper() in text.upper()):
            return w
    return ""
