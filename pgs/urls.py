from django.urls import path, include
from . views import PgsListView, PgsDetailView
from . import views


pgs_patterns = ([
    path('', views.PgsListView.as_view(), name='home'),
    path('pgs/<slug:slug>', views.PgsDetailView.as_view(), name='pg_detail')],
    'pgs')

urlpatterns = [
    path('', include(pgs_patterns)),
]
