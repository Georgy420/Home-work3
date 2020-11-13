def my_sum():
    sum_res = 0
    ex = False
    while not ex:
        number = input('Введите число / Q для выхода - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма чисел {sum_res}')
    print(f'Конечная сумма чисел {sum_res}')


my_sum()