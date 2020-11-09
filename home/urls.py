from django.urls import path
from home import views

urlpatterns = [
    path('', views.home,name='home'),
    path('cretae/', views.create,name='create'),
    path('vote/<poll_id>/', views.vote,name='vote'),
    path('result/<poll_id>/', views.result,name='result'),
]