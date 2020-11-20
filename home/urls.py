from django.urls import path
from home import views


admin.site.site_header="Poll Page Admin"
admin.site.site_title=" Welcome Divyansh"
admin.site.index_title="This is Poll Page Backend"

urlpatterns = [
    path('', views.home,name='home'),
    path('cretae/', views.create,name='create'),
    path('vote/<poll_id>/', views.vote,name='vote'),
    path('result/<poll_id>/', views.result,name='result'),
]
