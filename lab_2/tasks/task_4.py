def count_letters(msg):
    """
    Zwraca pare (znak, liczba zliczeń) dla najczęściej występującego znaku w wiadomości.
    W przypadku równości zliczeń wartości sortowane są alfabetycznie.

    :param msg: Message to count chars in.
    :type msg: str
    :return: Most frequent pair char - count in message.
    :rtype: list
    """
    s = list(set(list(msg)))
    counts = []
    for ss in s:
        count = 0
        for m in msg:
            if ss == m:
                count += 1
        counts.append(count)
    idx = counts.index(max(counts))
    return (s[idx], counts[idx])

if __name__ == '__main__':
    msg = 'Abrakadabra'
    assert count_letters(msg) == ('a', 4)
    assert count_letters('za') == ('a', 1)