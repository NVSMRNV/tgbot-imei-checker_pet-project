from django.urls import include, path

from api.views.checks import CreateIMEICheckAPIView
from api.views.services import ListIMEIServiceAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


imei_api_urlpatterns = [
    path('checks/', CreateIMEICheckAPIView.as_view(), name=''),
    path('services/', ListIMEIServiceAPIView.as_view(), name=''),
]


urlpatterns = [
    path('', include(imei_api_urlpatterns),),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
