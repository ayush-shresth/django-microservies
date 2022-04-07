from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_list, name='user_list'),
    path('user/<int:user_id>/', views.user_detail,name="user_detail"),
    path('user/update/', views.user_update, name='user_update'),
]