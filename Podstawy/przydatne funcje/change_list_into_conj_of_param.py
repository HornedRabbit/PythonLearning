def change_list_into_conj_of_param(my_list, key = "id"):
    conj_param = key + "="
    lastIterationNumber = len(my_list)
    i = 0
    for item in my_list:
        i += 1
        if (i == lastIterationNumber):
            conj_param += str(item)
        else:
            conj_param += str(item) + "&" + key + "="
        
    return conj_param
