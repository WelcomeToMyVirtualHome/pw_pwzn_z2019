def task_1():
    s = "\n"
    for i in range(1, 10, 1):
        s += str(i) * i
        s += "\n"
    return s
    
assert task_1() == '''
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''
