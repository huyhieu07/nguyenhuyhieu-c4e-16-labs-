def get_even_list(list):
    list02 = []
    for i in range(len(list)):
        if list[i] % 2 == 0:
            list02.append(list[i])
    list = list02
    return(list)
