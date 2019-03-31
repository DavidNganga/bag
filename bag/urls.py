from django.urls import path
from . import views


urlpatterns = [
    path('welcome/',views.welcome,name='welcome'),
    path('search/',views.search_results,name='search_results'),
]
