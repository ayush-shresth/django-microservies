
from django.urls import path
from . import views

urlpatterns = [
    path('content/<int:user_id>/<int:series_id>/',views.content, name='content'),
    path('content/update/', views.update, name='update'),
    path('content/load/', views.load, name='load'),
]
