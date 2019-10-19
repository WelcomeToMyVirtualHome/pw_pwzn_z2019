from task_1 import parse_input
from collections import defaultdict

def check_frequency(input):
  """
  Perform counting based on input queries and return queries result.

  Na wejściu otrzymujemy parę liczb całkowitych - operacja, wartość.
  Możliwe operacje:
  1, x: zlicz x
  2, x: usuń jedno zliczenie x jeżeli występuje w zbiorze danych
  3, x: wypisz liczbę zliczeń x (0 jeżeli nei występuje)
  Do parsowania wejścia wykorzystaj funkcję parse_input.
  Po wejściu (już jako liście) iterujemy tylko raz.
  Zbiór danych zrealizuj za pomocą struktury z collections.

  :param input: pairs of int: command, value
  :type input: string
  :return: list of integers with results of operation 3
  :rtype: list
  """

  parsed_input = parse_input(input)
  _dict = defaultdict(int)
  out = []
  for op, val in parsed_input:
    if op == 1:
      _dict[val] += 1
    elif op == 2:
      if val in _dict.keys():
        _dict[val] = max(_dict[val] - 1, 0)
    elif op == 3:
      if val not in _dict.keys():  
        out.append(0)
      else:
        out.append(_dict[val])
    else:
      print("Wrong operation number")
  return out

_input = """
1 5
1 6
3 2
1 10
1 10
1 6
2 5
3 2


"""
if __name__ == '__main__':  
  assert check_frequency(_input) == [0, 0]