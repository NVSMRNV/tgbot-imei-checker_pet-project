from django.urls import include, path

from api.views.services import ListIMEIServiceAPIView



imei_api_urlpatterns = [
    path('services/', ListIMEIServiceAPIView.as_view(), name=''),
]


urlpatterns = [
    path('imeis/', include(imei_api_urlpatterns),)
]
