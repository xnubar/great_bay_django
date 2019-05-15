from django.urls import path
from .views import *
urlpatterns = [
    path('signup/', registration, name = 'registration'),
    path('login/', login_view, name = 'login'),
    path('homepage/', homepage, name = 'homepage'),
    path('logout/', logout_view, name = 'logout'),
]
