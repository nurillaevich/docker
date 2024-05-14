from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='post'),
    path('<int:pk>/', PostDetail.as_view(), name='detail    ')
]
