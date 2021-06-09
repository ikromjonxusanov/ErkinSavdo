from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('explore/', explore, name="explore"),
    path('explore/<int:pk>/', detailExplore, name="exploreDetail"),
    path('login/', user_login, name="login"),
    path('signup/', signup, name="signup"),
    path('logout/', user_logout, name="logout"),
    path('profile/<str:username>/', profile, name='usersProfile'),
    path('profile/', profile, name='profile'),
    path('all/user/explore', user_all_ads, name='userAllAds'),
    path('add/home/', addHome, name="addHome"),
    path('profile/change/user/', changeProfile, name="changeProfile"),
    path('profile/change/password/', change_password, name="changePassword"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
