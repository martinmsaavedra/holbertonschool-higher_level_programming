def weight_average(my_list=[]):
    multi = 1.0
    mul = []
    final = []
    if not my_list:
        return 0
    else:
        for element in my_list:
            for i in range(len(element)):
                multi *= element[i]
                if i + 1 == len(element):
                    final.append(element[i])
                    mul.append(multi)
            multi = 1.0
        return float(sum(mul)) / float(sum(final))
