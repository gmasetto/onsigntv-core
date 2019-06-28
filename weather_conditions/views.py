from rest_framework.response import Response

from commons.responses import APIResponse
from commons.views import CustomAPIView
from .filters import WeatherConditionsFilter
from .services import GeocodeService


class WeatherConditions(CustomAPIView):
    filter_backends = [WeatherConditionsFilter]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = GeocodeService()

    def get(self, request):
        params = request.GET.dict()
        response = self.service.get_weather_conditions(params)
        return Response(APIResponse.result(data=response['temperature'], message=response['message']))
