def count_letters(msg):
    """
    Zwraca pare (znak, liczba zliczeń) dla najczęściej występującego znaku w wiadomości.
    W przypadku równości zliczeń wartości sortowane są alfabetycznie.

    :param msg: Message to count chars in.
    :type msg: str
    :return: Most frequent pair char - count in message.
    :rtype: list
    """
    
    dict_ = dict.fromkeys(list(msg))
    d = {key: (lambda words, letter: len([i for i, j in enumerate(words) if j == letter]))(msg, key) for key in dict_}
    d = {key : d[key] for key in sorted(d.keys())}
    key = max(d.keys(), key=(lambda key:d[key]))
    return (key, d[key])
    
if __name__ == '__main__':
    msg = 'Abrakadabra'
    assert count_letters(msg) == ('a', 4)
    assert count_letters('za') == ('a', 1)