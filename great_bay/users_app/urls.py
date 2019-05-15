from django.urls import path
from .views import *
urlpatterns = [
    path('signup/', registration, name = 'registration'),
    path('login/', login_view, name = 'login'),
    path('homepage/', homepage, name = 'homepage'),
    path('logout/', logout_view, name = 'logout'),
    # path('consumer/', consumer_view, name = 'consumer_profile'),
    path('owner/', owner_view, name = 'owner_profile'),
    # path('profile/', profile, name = 'profile'),
]
