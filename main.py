import re
import math
from tkinter import *
import time

# Задача №1 Найти площадь и периметр прямоугольного треугольника

def found_gepotenusa(a,b):
    c = math.sqrt(a**2 + b**2)
    result = (a * b) / 2
    P = a + b + c
    return result, P

a = float(input("Введите длину первого катета: "))
b = float(input("Введите длину второго катета: "))

triangle_P, triangle_result = found_gepotenusa(a, b)

print("Площадь треугольника = ", round(triangle_result, 2))
print("Периметр треугольника = ", round(triangle_P, 2))



# Задача №2 Найти корни квадратного уравнения

# ------------------------------------------------------------------------------------

print('Введите коэфициенты для уравнения...')
first = float(input('a = '))
second = float(input('b = '))
third = float(input('c = '))

discriminant = second**2 - 4 * first * third

print(discriminant)

if discriminant > 0 :
    x1 = (-second + math.sqrt(discriminant)) / (2 * first)
    x2 = (-second - math.sqrt(discriminant)) / (2 * first)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discriminant == 0:
    x = -second / (2 * first)
    print("x = %.2f" % x)
else:
    print('Корней нет ')


# ------------------------------------------------------------------------------------


# Задача №3.1 Сумма цифр трехзначного числа

number = float(input('введите трехзначное число:'))

d1 = number % 10
number = number // 10
d2 = number % 10
number = number // 10
print('Сумма равна = ' , number + d1 + d2)


# Задача №3.2 Сумма цифр трехзначного числа


n = input('введите трехзначное число:')
n1 = int(n[0])
n2 = int(n[1])
n3 = int(n[2])

print(n1+n2+n3)


# Задача №4 Обмен значений переменных

first_number = 14
second_number = 15
third_number = 16 

first_number, second_number, third_number = third_number, first_number, second_number

print(first_number,second_number,third_number)


# Задача №5 Найти площадь прямоугольника, треугольника или круга.


def rectangle_area(length, width):
    return round(length * width, 2) 

def triangle_area(a, b, c):
    perimetr = (a + b + c) / 2
    area = round(math.sqrt(perimetr * (perimetr - a) * (perimetr - b) * (perimetr - c)),2) 
    return area

def circle_area(radius):
    return round(math.pi * radius ** 2,2) 

def calculate_area():
    print("Выберите фигуру: 1: Прямоугольник, 2: Tреугольник, 3: Круг")
    choice = int(input("Введите номер: "))
    
    if choice == 1:
        length = float(input("Длина прямоугольника: "))
        width = float(input("Ширина прямоугольника: "))
        area = rectangle_area(length, width)
        print("Площадь прямоугольника:", area)
    elif choice == 2:
        number_a = float(input("Введите длину первой стороны: "))
        number_b = float(input("Введите длину второй стороны: "))
        number_c = float(input("Введите длину третьей стороны: "))
        area = triangle_area(number_a, number_b, number_c)
        print("Площадь треугольника:", area)
    elif choice == 3:
        radius = float(input("Введите радиус круга: "))
        area = circle_area(radius)
        print("Площадь круга:", area)
    else:
        print("Неверный выбор")

calculate_area()

# Задача №6

numbers = [2, 8, 15, 24, 37, 48, 137, 64, 80]

for number in numbers:
    if number % 2 == 0:
        print(number)  
    if number == 137:
        print("Встречено число 137. Программа остановлена.")
        break  

# Задача №7 

text = "Я к вам пишу — чего же боле? Что я могу еще сказать? Теперь, я знаю, в вашей воле Меня презреньем наказать."

text_with_replacement = text.replace('а', 'о')
replacement_count = text.count('а')

total_characters = sum(len(line) for line in text.split('\n'))

print("Текст с заменой буквы 'а' на 'о':")
print(text_with_replacement)
print("\nКоличество замен:", replacement_count)
print("Общее количество символов во всех строках:", total_characters)


# Задача №8

def sum_and_product_of_digits(number):
    number_str = str(number)
    
    digit_sum = 0
    digit_product = 1
    
    for digit_char in number_str:
        digit = int(digit_char)
        
        digit_sum += digit
        digit_product *= digit
    
    return digit_sum, digit_product

number_int = int(input("Введите целое число: "))

sum_of_digits, product_of_digits = sum_and_product_of_digits(number_int)

print("Сумма цифр числа:", sum_of_digits)
print("Произведение цифр числа:", product_of_digits)

# Задача №9

text_1 = "Python — это высокоуровневый язык программирования, отличающийся эффективностью, простотой и универсальностью использования. Он широко применяется в разработке веб-приложений и прикладного программного обеспечения, а также в машинном обучении и обработке больших данных."

word_count = len(text_1.split())

character_count = len(text_1)

print("Количество слов в тексте:", word_count)
print("Количество символов в тексте:", character_count)


# Задача №10


def calculator(expression):
    if not re.match("^[\d\s+\-*/().]*$", expression):
        return "Недопустимые символы в выражении"
    
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Ошибка: {e}"

while True:
    expression = input("Введите математическое выражение (для выхода введите 'exit'): ")

    if expression.lower() == "exit":
        print("Программа завершена.")
        break

    result = calculator(expression)
    print("Результат:", result)







