from . import views
from django.urls import path

urlpatterns = [
    path('daily_pass/unlock_chapter/<int:user_id>/<int:series_id>/', views.unlock_chapter, name='unlock_chapter'),
    path('daily_pass/chapter_detail/<int:user_id>/<int:series_id>/', views.chapter_detail, name='chapter_detail'),
    path('daily_pass/update/', views.user_update, name='user_update'),
    path('daily_pass/update_user/', views.user_update1, name='user_update1'),
    # path('daily_pass/user/<int:user_id>/<int:series_id>/', views.user_detail, name='user_detail'),
]