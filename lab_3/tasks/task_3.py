"""
Zadanie za 2 pkt.

Uzupełnij funckję parse_dates tak by zwracała przygotowaną wiadomość
z posortowanymi zdarzeniami.
Funkcja przyjmuje ciag zdarzeń (zapisanych w formie timestampu w dowolnej strefie czasowej),
przetwarza je na zdarzenia w strefie czasowej UTC i sortuje.
Posortowane zdarzenia są grupowane na dni i wypisywane od najnowszych do najstarszych.

Na 1pkt. Uzupełnij funkcję sort_dates, która przyjmuje dwa parametry:
- log (wielolinijkowy ciąg znaków z datami) zdarzeń
- format daty (podany w assercie format ma być domyślnym)
Zwraca listę posortowanych obiektów typu datetime w strefie czasowej UTC.

Funkcje group_dates oraz format_day mają pomoc w grupowaniu kodu.
UWAGA: Proszę ograniczyć użycie pętli do minimum (max 4).
"""
from datetime import datetime, tzinfo, timezone
from itertools import groupby

def sort_dates(date_str, date_format=''):
    """
    Parses and sorts given message to list of datetimes objects descending.

    :param date_str: log of events in time
    :type date_str: str
    :param date_format: event format
    :type date_format: str
    :return: sorted desc list of utc datetime objects
    :rtype: list
    """
    str_stripped = date_str.strip().splitlines()
    dates = list(map(lambda x: datetime.strptime(x, date_format), str_stripped))
    dates = [ (x - x.utcoffset()).replace(tzinfo = timezone.utc) for x in dates]
    
    return sorted(dates, reverse = True)

def group_dates(dates):
    """
    Groups list of given days day by day.

    :param dates: List of dates to group.
    :type dates: list
    :return:
    """

    sorted_dates = sorted(dates, reverse = True)
    grouped_dates = groupby(sorted_dates, key = lambda x: x.strftime('%Y-%m-%d'))
    return grouped_dates

def format_day(day, events):
    """
    Formats message for one day.

    :param day: Day object.
    :type day: datettime.datetime
    :param events: List of events of given day
    :type events: list
    :return: parsed message for day
    :rtype: str
    """
    formatted_day = f"{day}"
    for e in events:
        formatted_day += f"\n\t{e.strftime('%H:%M:%S')}"
    return formatted_day


def parse_dates(date_str, date_format=''):
    """
    Parses and groups (in UTC) given list of events.

    :param date_str: log of events in time
    :type date_str: str
    :param date_format: event format
    :type date_format: str
    :return: parsed events
    :rtype: str
    """
    sorted_dates = sort_dates(dates, date_format)
    grouped_dates = group_dates(sorted_dates)
    formatted_events = ""
    break_str = "\n----\n"
    for day, events in grouped_dates:
        formatted_events += f"{format_day(day, events)}" + break_str
    return formatted_events[:-len(break_str)]
    

if __name__ == '__main__':
    dates = """
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
"""

assert sort_dates(dates, '%a %d %B %Y %H:%M:%S %z') == [
    datetime(2015, 5, 10, 20, 54, 36, tzinfo=timezone.utc),
    datetime(2015, 5, 10, 13, 54, 36, tzinfo=timezone.utc),
    datetime(2015, 5, 2, 14, 24, 36, tzinfo=timezone.utc),
    datetime(2015, 5, 1, 13, 54, 36, tzinfo=timezone.utc),
]

assert parse_dates(dates, '%a %d %B %Y %H:%M:%S %z') == """2015-05-10
\t20:54:36
\t13:54:36
----
2015-05-02
\t14:24:36
----
2015-05-01
\t13:54:36"""
