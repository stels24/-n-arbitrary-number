def test(*params):
    print("Appl", "orange", 1, 2, 3, *params)
    print(True, 10, 11, 2 *params)
    print(2, 2, 2 *params)

test(4, 5, 6)

# Факториал числа n — это произведение всех натуральных чисел от единицы до n.

def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number - 1)


print(factorial(int(input('Введите число: '))))