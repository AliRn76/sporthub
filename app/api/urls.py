
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from app.api.views import main_view, signup_view, show_all_clubs_view, show_club_view, \
    show_club_sans


app_name = "api"

urlpatterns = [
    path('', main_view, name='main'),
    path('signup/', signup_view),
    path('login/', obtain_auth_token),
    path('show-all-clubs/', show_all_clubs_view),
    path('club/', show_club_view),
    path('club-sans/', show_club_sans),

]
