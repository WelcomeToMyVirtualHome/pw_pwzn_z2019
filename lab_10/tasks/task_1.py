import requests
from urllib.parse import urljoin

API_URL = 'https://www.metaweather.com/api/'

def get_cities_woeid(query: str, timeout: float = 5.):    
    location_url = urljoin(API_URL, 'location/search')
    data = None
    try:
        response = requests.get(location_url, params=dict(query=query), timeout=timeout)
    except requests.exceptions.Timeout:
        print(f'Request for: {location_url} took to long!')
    else:
        print(f'Status code: {response.status_code}, Took: {response.elapsed}')
        try: 
            response.raise_for_status()
        except requests.exceptions.HTTPError as e: 
            print(e)
        data = {}
        try:
            json_response = response.json()
        except RuntimeError as e:
            print(e)
        finally:
            for r in json_response:
                data[r['title']] = r['woeid']
    finally:
        return data

if __name__ == '__main__':
    assert get_cities_woeid('Warszawa') == {}
    assert get_cities_woeid('War') == {
        'Warsaw': 523920,
        'Newark': 2459269,
    }
    try:
        get_cities_woeid('Warszawa', 0.1)
    except Exception as exc:
        isinstance(exc, requests.exceptions.Timeout)
