import random
def meets_conditions(number):
    return number > 10 and number % 2 != 0
def genrandomnum(count, lower, upper):
    validnumbers = []
    while len(validnumbers) < count:
        num = random.randint(0, 30000)
        if meets_conditions(num):
            validnumbers.append(num)
    return validnumbers
count = 30
lower = 0
upper = 3000
validnumbers = genrandomnum(count, lower, upper)
print("Random Numbers greater than 10 and odd:", validnumbers)
    