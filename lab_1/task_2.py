def task_2():
    s = "\n"
    for i in range(1, 6, 1):
        s += "*" * i + "\n"
    for i in range(4, 0, -1):
        s += "*" * i + "\n"
    return s
print(task_2())

assert task_2() == '''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''