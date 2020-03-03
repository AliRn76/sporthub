
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from app.api.views import signup_view, show_all_clubs_view


app_name = "api"

urlpatterns = [
    path('signup/', signup_view),                   # http://127.0.0.1:8040/api/signup
    path('login/', obtain_auth_token),              # http://127.0.0.1:8040/api/login
    path('show-all-clubs/', show_all_clubs_view),   # http://127.0.0.1:8040/api/show-all-clubs

]
