def str_list(string):
    char_list = list(string)
    int_list = []
    
    for i in char_list:
        try:
            int_list.append(int(i))
        except:
            pass

    return int_list
