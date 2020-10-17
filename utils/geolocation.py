import requests

from InfectionPrevention.settings import get_secret


def fetch_coordinates(place):
    apikey = get_secret(["CART_API_KEY"])
    base_url = "https://geocode-maps.yandex.ru/1.x"
    params = {"geocode": place, "apikey": apikey, "format": "json"}
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    places_found = response.json()['response']['GeoObjectCollection']['featureMember']
    most_relevant = places_found[0]
    coords = most_relevant['GeoObject']['Point']['pos'].replace(' ', ',')
    return coords

def fetch_district(place):
    apikey = get_secret(["CART_API_KEY"])
    coords = fetch_coordinates(place)
    base_url = "https://geocode-maps.yandex.ru/1.x"
    params = {"geocode": coords, "apikey": apikey, "format": "json", "kind": "district"}
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    places_found = response.json()['response']['GeoObjectCollection']['featureMember']
    most_relevant = places_found[0]
    district = most_relevant['GeoObject']['name']
    okrug = most_relevant['GeoObject']['description']
    return district, okrug