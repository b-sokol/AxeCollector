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
  path('axes/<int:axe_id>/add_axe_photo/', views.add_axe_photo, name='add_axe_photo'),
  path('axes/<int:axe_id>/assoc_string/<int:string_id>/', views.assoc_string, name='assoc_string'),
  path('axes/<int:axe_id>/curr_string/<int:string_id>/', views.curr_string, name='curr_string'),
  path('axes/<int:axe_id>/remove_string/<int:string_id>/', views.remove_string, name='remove_string'),
  path('strings/', views.StringList.as_view(), name='strings_index'),
  path('strings/<int:pk>/', views.StringDetail.as_view(), name='strings_detail'),
  path('strings/<int:pk>/add_string_photo/', views.add_string_photo, name='add_string_photo'),
  path('strings/create/', views.StringCreate.as_view(), name='strings_create'),
  path('strings/<int:pk>/update/', views.StringUpdate.as_view(), name='strings_update'),
  path('strings/<int:pk>/delete/', views.StringDelete.as_view(), name='strings_delete'),
]
