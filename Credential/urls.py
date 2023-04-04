from django.urls import path
from . import views
app_name = 'Credential'
urlpatterns = [
    path('registerUser/', views.registerUser, name='registerUser'),
    path('userLogin/', views.userLogin, name='userLogin'),
    path('logout/', views.logout, name='logout'),
]