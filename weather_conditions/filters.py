import coreapi
from rest_framework.filters import BaseFilterBackend


class WeatherConditionsFilter(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [
            coreapi.Field(
                name='key_google',
                required=True,
                type='string',
                description='key client'
            ),
            coreapi.Field(
                name='key_darksky',
                required=True,
                type='string',
                description='key client'
            ),
            coreapi.Field(
                name='zipcode',
                required=True,
                type='string',
                description='weather_conditions'
            ),
        ]
