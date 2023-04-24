# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def degree(numb_a, numb_b):
    if numb_b == 1:
        return numb_a
    return numb_a * degree(numb_a, numb_b - 1)

print(degree(3, 5))