def sum_list(*args):
    ret_list = []
    summ = 0
    for i in range(len(args[0][:])):
        for j in range(len(args[:][:])):
            summ += args[j][i]
        ret_list.append(summ)
        summ = 0

    return ret_list
