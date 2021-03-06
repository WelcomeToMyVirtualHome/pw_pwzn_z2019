def stack_operation(stack_commands):
    """
    Funkcja przyjmuję listę jedno i dwu elementowych krotek - operacji na stosie.
    Pierwszy element krotki to operacja, drugi wartość (opcjonalnie). Operacje:
    push - dodaj element do stosu
    pop - usuń element ze stosu
    show_max - wypisz maksymalny element w stosie
    Uzupełnij funkcje tak, by dla podanej zwróciła ciąg maksymalnych elementów (zgodny z liczbą operacj 3).

    :param stack_commands: List of tuples of stack commands.
    :type stack_commands: list
    :return: List of outputs from commands.
    :rtype: list
    """
    stack = []
    for c in stack_commands:
        if c[0] == 'push':
            stack.append(c[1])
        elif c[0] == 'pop':
            stack.pop()
        elif c[0] == 'show_max':
            max(stack)
        else:
            print("Unknown command, doing nothing")
    return stack

if __name__ == "__main__":
    commands = [
        ('push', 97),
        ('pop',),
        ('push', 20), 
        ('pop',), 
        ('push', 26), 
        ('push', 20), 
        ('pop',), 
        ('show_max',), 
        ('push', 91), 
        ('show_max',)
    ]
    assert stack_operation(commands) == [26, 91]
