import pathlib
from typing import Optional, Union, List
from urllib.parse import urljoin
import requests
import os
import csv

API_URL = 'https://www.metaweather.com/api/'

def get_city_data(
    woeid: int,
    year: int,
    month: int,
    path: Optional[Union[str, pathlib.Path]] = None,
    timeout: float = 5.0,
) -> (str, List[str]):
    if isinstance(path, pathlib.PosixPath):
        save_path = path
    elif isinstance(path, str):
        save_path = pathlib.PosixPath(path) / f'{woeid}_{year}_{month:02}'
    else:
        save_path = pathlib.Path.cwd() / f'{woeid}_{year}_{month:02}'

    newdir = os.path.dirname(str(save_path) + '/')
    if not os.path.exists(newdir):
        os.makedirs(newdir)
        
    session = requests.session()
    stored_files = []
    for day in range(1, 32):
        print(f'Downloading data for {woeid}/{year}/{month}/{day}')
        location_url = urljoin(API_URL, f'location/{woeid}/{year}/{month}/{day}')
        try:
            response = session.get(location_url, timeout=timeout)
        except requests.exceptions.Timeout:
            print(f'Request for: {location_url} took to long!')
        else:
            try: 
                response.raise_for_status()
            except requests.exceptions.HTTPError as e: 
                print(e)
            try:
                json_response = response.json()
            except RuntimeError as e:
                print(e)
            finally:
                if json_response:
                    with open(save_path / f"{year}_{month:02}_{day:02}.csv", mode="w+") as f:
                        writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        first_row = True
                        for row in json_response: 
                            if first_row:
                                first_row = False
                                writer.writerow(row.keys())
                            writer.writerow(row.values())
                        stored_files.append(save_path / str(day))
    return str(save_path), stored_files

if __name__ == '__main__':
    _path = pathlib.Path.cwd()
    expected_path = _path / '523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3)
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert str(expected_path) == dir_path

    expected_path = 'weather_data/523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3, path='weather_data')
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path

    expected_path = 'weather_data/523920_2012_12'
    dir_path, file_paths = get_city_data(523920, 2012, 12, path='weather_data')
    assert len(file_paths) == 0
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path