from django.contrib import admin

from app.models import (
    Admin,
    Client,
    Clubowner,
    Club,
    Clubsans,
    Clubpictures,
    Clubscore,
    Comments,
    Rent,

    )
admin.site.register(Admin)
admin.site.register(Client)
admin.site.register(Clubowner)
admin.site.register(Club)
admin.site.register(Clubpictures)
admin.site.register(Clubsans)
admin.site.register(Clubscore)
admin.site.register(Comments)
# admin.site.register(Rent)
# admin.site.register(Team)
# admin.site.register(TeamMember)

