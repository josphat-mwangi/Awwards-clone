from django.urls import path
from django.conf.urls import url
from . import views
from .views import (PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView)

urlpatterns = [
   path('', views.index, name='index'),
   path('register/', views.register, name='register'),
   url(r'^profile/(\d)$', views.profile, name='profile'),
   path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
   path('post/new/', PostCreateView.as_view(), name='post-create'),
   path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
   path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
