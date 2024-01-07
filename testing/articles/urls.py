from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='articles'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
  #  path("search/", views.Search.as_view(), name='search')
]


