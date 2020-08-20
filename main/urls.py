from django.urls import path
from django.conf.urls import url
from . import views
from .views import (PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('', views.index, name='index'),
   path('register/', views.register, name='register'),
   url(r'^profile/(\d)$', views.profile, name='profile'),
   path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
   path('post/new/', PostCreateView.as_view(), name='post-create'),
   path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
   path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
   path('search/', views.search_results, name='search_results'),
   url(r'^site/(\d+)', views.site, name='site'),
   url(r'^api/users/$', views.UserList.as_view()),
   url(r'^api/projects/$', views.ProjectList.as_view()),
   url(r'^api/ratings/$', views.RatingList.as_view())
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
