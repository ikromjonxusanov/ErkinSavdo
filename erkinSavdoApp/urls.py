from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('houses/', houses, name="houses"),
    path('houses/<int:pk>/', house, name="house"),
    path('login/', user_login, name="login"),
    path('signup/', signup, name="signup"),
    path('logout/', user_logout, name="logout"),
    path('profile/<str:username>/', profile, name='usersProfile'),
    path('profile/', profile, name='profile'),
    path('profile/all/houses/', user_all_ads, name='userAllAds'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
