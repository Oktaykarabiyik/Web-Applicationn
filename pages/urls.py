from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# http://127.0.0.1:8000/

urlpatterns=[
     path('',views.index,name='index'),
     path('admin',views.index,name='admin'),          #views.index
    # path('about',views.about,name='about'),
]
