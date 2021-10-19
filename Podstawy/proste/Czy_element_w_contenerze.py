import time

"FUNCTION_TIMER//////////////////////////////////////"
def function_perf(func, *arg, how_many_times = 1):
    sum = 0
    for i in range (0, how_many_times):
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sum += (end - start)
    return sum


setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]


"CHECK_IF_ITEM_IN_CONTAINER//////////////////////////////"
def check_if_item_in(item, container):
    if item in container:
        return True
    else:
        return False    




print(check_if_item_in(30, setContainer))
print(function_perf(check_if_item_in, 30, setContainer))


"""
print(check(30,listContainer))
print(function_perf(check, (30, listContainer))      
"""      

