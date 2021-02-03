from django.urls import path
from .views import HomePageView, PostDetailView, NewPostView, UpdatePostView,DeletePostView

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(),name='post-delete'),
    path('post/<int:pk>/update/', UpdatePostView.as_view(), name='post-update'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', NewPostView.as_view(), name='new-post')
]
