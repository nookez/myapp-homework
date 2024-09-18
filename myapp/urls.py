from django.contrib import admin
from django.urls import path
from . import views
from .views import index, detail1, detail2, detail3, detail4

urlpatterns = [
    path('', index, name='index'),  
    path('home/', views.home_view, name='home'), 
    path('detail1/', detail1, name='detail1'),
    path('detail2/', detail2, name='detail2'),  
    path('detail3/', detail3, name='detail3'), 
    path('detail4/', detail4, name='detail4'), 
    path('admin/', admin.site.urls),
]