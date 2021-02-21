from django.urls import path,include
# from .views import HomePageView,contact
from .views import homepage


urlpatterns = [
    path('',homepage,name='home'),
    # path('databasemap/',databaseshow,name='dbshow'),    
]