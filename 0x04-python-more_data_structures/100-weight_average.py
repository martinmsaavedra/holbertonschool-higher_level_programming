def weight_average(my_list=[]):
    suma = 0
    divisor = 0
    if my_list:
        for i in my_list:
            suma += (i[0] * i[1])
        for i in my_list:
            divisor += i[1]
        return suma / divisor
    else:
        return 0
