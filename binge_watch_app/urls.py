# binge_watch_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Main dashboard view
    path('', views.content_list, name='content_list'),
    
    # 🌟 NEW: Path to add or edit a review for a specific piece of content 🌟
    path('review/add/<int:content_id>/', views.add_review, name='add_review'),
]