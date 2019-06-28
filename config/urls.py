from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
schema_view = get_swagger_view(title='API')

api_v1_urlpatterns = [
    url(r'geocodes/?', include('weather_conditions.urls')),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls, namespace=None)),
    url(r'^api-auth/', include('rest_framework.urls', namespace=None)),
    url(r'^v1/', include(api_v1_urlpatterns, namespace=None)),
    url(r'^docs/', schema_view)
]
