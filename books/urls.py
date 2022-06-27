from django.urls import path
from . import views
app_name = 'books'
urlpatterns = [
    #Home Page
    path('', views.index, name = 'index'),
    path('home/' ,views.home, name = 'home'),
    path('home/borrow' ,views.borrow, name = 'borrow'),
    path('home/borrow/home2',views.home2),
]
