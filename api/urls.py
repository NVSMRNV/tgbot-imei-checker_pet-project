from django.urls import include, path

from api.views.checks import CreateIMEICheckAPIView
from api.views.services import ListIMEIServiceAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.views.users import AcceptUserAPIView, ListCreateUserAPIView


imei_api_urlpatterns = [
    path('checks/', CreateIMEICheckAPIView.as_view(), name='imei_checks_create'),
    path('services/', ListIMEIServiceAPIView.as_view(), name='imei_services_list'),
]

users_api_urlpatterns = [
    path('users/whitelist/', AcceptUserAPIView.as_view(), name='users_whitelist'),
    path('users/', ListCreateUserAPIView.as_view(), name='users_list_create'),
]

urlpatterns = [
    path('', include(imei_api_urlpatterns),),
    path('', include(users_api_urlpatterns)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
