import random
n = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
def ram():
    now = random.choice(n)
    return now
def first(number):
    password = ""
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                password += str(i) + str(j)
    return password
now = ram()
result1 = first(now)
print("Код =", now)
print("Пароль =", result1)