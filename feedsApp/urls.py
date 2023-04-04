from django.urls import path
from . import views
app_name = 'feedsApp'
urlpatterns = [
    path('', views.feed, name='home'),
    path('profile/', views.profile, name='profile'),
    path('add/', views.add, name='add'),
    path('addProject/', views.addProject, name='addProject'),
    path('<slug:slug>/', views.showCmt, name='showComment'),
    path('addCmt/<int:id>/', views.addCmt, name='addCmt'),

]