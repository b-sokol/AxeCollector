from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('axes/', views.axes_index, name='index'),
  path('axes/<int:axe_id>/', views.axes_detail, name='detail'), 
  path('axes/create/', views.AxeCreate.as_view(), name='axes_create'),
  path('axes/<int:pk>/update/', views.AxeUpdate.as_view(), name='axes_update'),
  path('axes/<int:pk>/delete/', views.AxeDelete.as_view(), name='axes_delete'),
  path('axes/<int:axe_id>/add_maintenance/', views.add_maintenance, name='add_maintenance'),
]
