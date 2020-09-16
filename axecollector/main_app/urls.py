from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('axes/', views.axes_index, name='index'),
    path('axes/<int:axe_id>/', views.axes_detail, name='detail'),
]
