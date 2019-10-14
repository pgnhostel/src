from django.urls import path, include
from . views import FaqListView
from . import views


faq_patterns = ([path('', views.FaqListView.as_view(), name='faq')], 'faq')

urlpatterns = [
    path('', include(faq_patterns)),
    ]
