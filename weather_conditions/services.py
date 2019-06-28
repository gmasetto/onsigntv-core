from http import HTTPStatus

import requests


class GeocodeService:
    def get_weather_conditions(self, params):
        url = '{url}={key}&address={zipcode}'.format(
            url='https://maps.googleapis.com/maps/api/geocode/json?key',
            key=params['key_google'], zipcode=params['zipcode'])

        response = requests.get(url, headers={'Content-Type': 'application/x-www-form-urlencoded'})

        if response.status_code == HTTPStatus.OK.value and len(response.json()['results']) > 0:
            coordinates = response.json()['results'][0]['geometry']['location']

            url = '{url}{key}/{lat},{lng}'.format(
                url='https://api.darksky.net/forecast/',
                key=params['key_darksky'], lat=coordinates['lat'], lng=coordinates['lng'])

            response = requests.get(url, headers={'Content-Type': 'application/x-www-form-urlencoded'})

            if response.status_code == HTTPStatus.UNAUTHORIZED.value:
                return dict(temperature=0, message="Problem finding temperature")

            return dict(temperature=((response.json()['currently']['temperature'] - 32) * 5 / 9),
                        message="Temperature was found")

        return dict(temperature=0, message="Problem finding temperature")
