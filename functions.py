# decorator
def dec(say_hello):
    def wrap():
        print("--")
        say_hello()
        print("--")
    return wrap


@dec
def say_hello():
    print("Hello")


def foo_many(*args, **kwargs):
    print(args, kwargs, sep="\n")

# foo_many(1, "2", fff="123123", aaa=52353)

f = lambda x, y: x + y
# print(f(1, 5))

# --------- Tasks ----------


# empry function
def empty_foo():
    pass


# multiply on two
def mul_two(arg):
    return arg * 2


# check on even
def even_num(arg):
    if arg % 2 == 0:
        print("yes")
    else:
        print("no")


# more than ten?
def comp_ten(arg1, arg2):
    if arg1 > 10:
        print("yes")
    else:
        print("no")


# lambda function mod
div_mod = lambda x, y: x % y
# print(div_mod(4, 3))


# decorator
def dec_easy_comands(easy_comands):
    def wrap(arg):
        print("line above")
        easy_comands(arg)
        print("lime below")
    return wrap


# function which decorated
@dec_easy_comands
def easy_comands(arg1):
    print(arg1 ** 5)


# input numbers from keyboard with map and filter
# list_num = list(map(int, input().split(" ")))
# print(list_num)


# clean function
def clean_foo(arg1, arg2):
    a = arg1 + arg2
    return a ** 2

CONST = 5


# unclean function
def dirty_foo(arg):
    a = CONST + arg
    return a ** 2


# search max and min in list
def find_minmax(my_list):
    min = my_list[0]
    max = my_list[0]
    for i in my_list:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max

# print(find_minmax([4, 5, -2, 56, 0, -55]))


# check year on leap
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

# leap_year(2100)


# define season
def season(month):
    if month <= 2 or month == 12:
        return "Winter!"
    elif month <= 5:
        return "Spring!"
    elif month <= 8:
        return "Summer!"
    elif month <= 11:
        return "Autumn!"

# print(season(5))


# check on true date
def date(day, month, year):
    if leap_year(year) is True:
        if (
                month == 1 or month == 3 or month == 5 or month == 7 or
                month == 8 or month == 10 or month == 12):
            if day <= 31 and day >= 0:
                return True
            else:
                return False
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day <= 30 and day >= 0:
                return True
            else:
                return False
        elif month == 2:
            if day <= 29 and day >= 0:
                return True
            else:
                return False
        else:
            return False
    else:
        if (
                month == 1 or month == 3 or month == 5 or month == 7 or
                month == 8 or month == 10 or month == 12):
            if day <= 31 and day >= 0:
                return True
            else:
                return False
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day <= 30 and day >= 0:
                return True
            else:
                return False
        elif month == 2:
            if day <= 28 and day >= 0:
                return True
            else:
                return False
        else:
            return False

# print(date(29, 2, 2400))


# selection num from list and then sort them
def selectin_num(my_list):
    new_list = list()
    for i in my_list:
        if type(i) == int or type(i) == float:
            new_list.append(i)
    new_list.sort()
    return new_list

# print(selectin_num([16, -17, 2, 78.7, False, False, {'True': True}, 555, 12, 23, 42, 'DD']))
