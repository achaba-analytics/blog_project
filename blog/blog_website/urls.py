from django.urls import path
#from . import views
from .views import HomeView, ArticleView, AddPostView, UpdateView, AddCategoryView, CategoryView, CategoryListView, LikeView, DeleteView #delete_article

urlpatterns = [
    #path('', views.home, name='home')
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>',ArticleView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdateView.as_view(), name='update'),
    path('article/<int:pk>/delete', DeleteView.as_view(), name='delete'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category_list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    #path('delete/<int:pk>/', delete_article, name='delete'),
]