"""
Задача 2.

За багато років ув’язнення в’язень замку Іф зробив у стіні
прямокутний отвір розміром d × e. Замок Іф побудований із цегли,
розміром a × b × c. Визначте, чи зможе в’язень викидати цеглини
в море через цей отвір (сторони цегли є паралельними сторонам
отвору). Програма отримує на вхід числа a, b, c, d, e і повинна
вивести слово Yes або No.

Автор: Новосад Сніжана
"""

# Введення розмірів цегли та отвору від користувача
a = int(input("Введіть розмір a цегли: "))
b = int(input("Введіть розмір b цегли: "))
c = int(input("Введіть розмір c цегли: "))
d = int(input("Введіть розмір d отвору: "))
e = int(input("Введіть розмір e отвору: "))


# Перевірка можливості викидання цеглин
if (a <= d and b <= e) or (b <= d and a <= e):
    print("Yes")
elif (a <= d and c <= e) or (c <= d and a <= e):
    print("Yes")
elif (b <= d and c <= e) or (c <= d and b <= e):
    print("Yes")
else:
    print("No")
