def func1():
    three_numbers = [int(i) for i in input().split(" ")]
    # print(three_numbers)
    f = False
    for i in range(len(three_numbers) - 1):
        for j in range(i + 1, len(three_numbers)):
            if three_numbers[i] == three_numbers[j]:
                print("yes")
                f = True
                break
        if f is True:
            break
    if f is False:
        print("ERROR")


def func2():
    three_numbers = [int(i) for i in input().split(" ")]
    if three_numbers[0] + three_numbers[1] == three_numbers[2]:
        print("yes")
    elif three_numbers[1] + three_numbers[2] == three_numbers[0]:
        print("yes")
    elif three_numbers[0] + three_numbers[2] == three_numbers[1]:
        print("yes")
    else:
        pass


def sum(fr, t):
    res = 0
    for i in range(fr, t + 1):
        res += i
    print(res)


def day_of_week():
    days = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 7
    }
    for key, value in days.items():
        if value == 6 or value == 7:
            print("%s - %s day of week (%s)" % (key, value, "holyday"))
        else:
            print("%s - %s day of week (%s)" % (key, value, "workday"))

day_of_week()
