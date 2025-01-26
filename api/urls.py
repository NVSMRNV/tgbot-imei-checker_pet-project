from django.urls import include, path

from api.views.checks import CreateIMEICheckAPIView
from api.views.services import ListIMEIServiceAPIView



imei_api_urlpatterns = [
    path('checks/', CreateIMEICheckAPIView.as_view(), name=''),
    path('services/', ListIMEIServiceAPIView.as_view(), name=''),
]


urlpatterns = [
    path('imeis/', include(imei_api_urlpatterns),)
]
