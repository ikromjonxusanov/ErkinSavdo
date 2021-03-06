from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('explore/', explore, name="explore"),
    path('explore/<int:pk>/', detailExplore, name="exploreDetail"),
    path('explore/<int:pk>/edit/', updateHome, name="exploreDetailUpdate"),
    path('login/', user_login, name="login"),
    path('signup/', signup, name="signup"),
    path('logout/', user_logout, name="logout"),
    path('profile/<str:username>/', profile, name='profile'),
    path('profile/<str:username>/explore/', user_all_homes, name='userAllHomes'),
    path('add/home/', addHome, name="addHome"),
    path('profile/change/user/', changeProfile, name="changeProfile"),
    path('profile/change/password/', change_password, name="changePassword"),
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)