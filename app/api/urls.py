
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from app.api.views import (

    registration_view,
    show_all_clubs_view
    )

app_name = "api"

urlpatterns = [
    path('register', registration_view),
    path('login', obtain_auth_token),
    path('show-all-clubs/', show_all_clubs_view),

]
