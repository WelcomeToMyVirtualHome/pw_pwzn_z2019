import filecmp
import pathlib
import pandas as pd
from typing import Union
from os.path import isfile, join
from os import listdir

def concat_data(path: Union[str, pathlib.Path],):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    select_cols = ['created', 'min_temp', 'the_temp', 'max_temp', 'air_pressure', 'humidity', 'visibility', 'wind_direction_compass', 'wind_direction', 'wind_speed']
    _data = None
    for file_ in files:
        day = int(file_.split('_')[2].split('.')[0])
        data = pd.read_csv(pathlib.Path(path) / file_) 
        data = data[select_cols]
        data.rename(columns={'the_temp':'temp'}, inplace=True)
        data.created = pd.to_datetime(data.created)
        data = data[data.created.dt.day == day]
        if _data is not None:
            _data = _data.append(data.copy()) 
        else:
            _data = data.copy()
    _data.sort_values(['created'], inplace=True)
    _data.created = _data.created.dt.strftime('%Y-%m-%dT%H:%M')
    with open(str(path) + '.csv', 'w+') as f:
        f.write(_data.to_csv(index=False))

if __name__ == '__main__':
    concat_data('weather_data/523920_2017_03')
    assert filecmp.cmp(
        'expected_523920_2017_03.csv',
        'weather_data/523920_2017_03.csv'
    )
