from django.urls import path, include
from rest_framework_simplejwt import views as auth_views
from .views import UserCreateAV

auth_urlpatterns = [
    path(
        'token/',
        auth_views.TokenObtainPairView.as_view(),
        name='token-obtain-pair'
    ),

    path(
        'refresh/',
        auth_views.TokenRefreshView.as_view(),
        name='token-refresh'
    )
]

# TODO
user_urlpatterns = [
    path('create/', UserCreateAV.as_view()),  # api/users/users/create
]

app_name = 'users'
urlpatterns = [
    path('auth/', include(auth_urlpatterns)),
    path('users/', include(user_urlpatterns))
]
