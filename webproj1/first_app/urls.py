from django.urls import path
from .views import view_airport,view_login,view_home,LogoutView
urlpatterns=[
    path('',view_home,name='home'),
    path('login/',view_login,name='login'),
    path('logout/',LogoutView.as_view(next_page=reversed('login')),name='logout')
]