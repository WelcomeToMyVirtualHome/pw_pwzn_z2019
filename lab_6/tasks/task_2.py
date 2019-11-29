"""
Na (1 pkt.):
Napisz program do sprawdzenia poprawności skompresowanego wyjścia poprzedniej
funkcji.
Funkcja MUSI w swej implementacji korzystać z wyrażeń regularnych.

Funkcja na wejściu przyjmuje nazwę pliku do sprawdzenia, na wyjściu zwraca
dwuelementową tuplę zawierającą liczbę poprawnych wierszy:
- na indeksie 0 płeć F
- na indeksie 1 płeć M
"""
import re
import pandas as pd

def match_msg(pattern, msg):
    return bool(re.fullmatch(pattern, msg))

def check_animal_list(file_path):
    with open(file_path) as _input:
        lines = _input.readlines()
        
    m_count, f_count = 0, 0
    m_pattern = r'^[a-fA-F\d]{8}\-[a-fA-F\d]{4}\-[a-fA-F\d]{4}\-[a-fA-F\d]{4}\-[a-fA-F\d]{12}_M_[\d]\.[\d]{3}e[\-\+][\d]{2}$'
    f_pattern = r'^[a-fA-F\d]{8}\-[a-fA-F\d]{4}\-[a-fA-F\d]{4}\-[a-fA-F\d]{4}\-[a-fA-F\d]{12}_F_[\d]\.[\d]{3}e[\-\+][\d]{2}$'
    for line in lines:
        line = line.strip()
        m_count += match_msg(m_pattern, line)
        f_count += match_msg(f_pattern, line)
    print((f_count, m_count))
    return (f_count, m_count)

if __name__ == '__main__':
    assert check_animal_list('s_animals_sce.txt') == (2, 2)
    assert check_animal_list('animals_sc_corrupted.txt') == (5, 0)
