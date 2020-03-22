from django.conf.urls import url
from django.conf.urls.static import static

from djangoProjectTest import settings
from landing import views

urlpatterns = [
    url(r'^', views.home, name='home'),
    url(r'^landing/', views.landing, name='landing')
]


