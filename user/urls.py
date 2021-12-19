from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('login/<str:pk>', views.login, name= 'login'),
    path('logout/', views.logout, name= 'logout'),
    path('about',views.about,name='about'),
    path('pdfs/<int:pk>/',views.delete_pdf,name='delete_pdf'),
    path('pdfs/',views.pdf_list,name='pdf_list'),
    path('pdfs/upload/',views.upload_pdf,name='upload_pdf'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)