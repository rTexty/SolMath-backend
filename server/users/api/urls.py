from django.urls import path, include
from rest_framework_simplejwt import views as auth_views

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

]

app_name = 'users'
urlpatterns = [
    path('auth/', include(auth_urlpatterns)),
    path('', include(user_urlpatterns))
]
