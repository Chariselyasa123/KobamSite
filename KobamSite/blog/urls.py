from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('about/', views.about, name='about-home'),
    path('materi/', views.menu_materi, name='menu-materi'),
    path('materi/pendahuluan/', views.materi_cpp_pendahuluan, name='pendahuluan')
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)