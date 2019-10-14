from django.urls import path, include
from . import views

personal_patterns = ([
    path('', views.index, name='index'),
    path('personal/about', views.about, name='about'),
    path('personal/contact', views.contact, name='contact')], 'personal')

urlpatterns = [
    path('', include(personal_patterns))
]
