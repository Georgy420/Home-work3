def sum(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Неправильное значение!\nВы не можете использовать 0 в качестве разделителя")
        return


a, b = (int(digit) for digit in input("Введите 2 числа через пробел: ").split())
print(sum(a, b))

