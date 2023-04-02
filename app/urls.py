from django.urls import path
from .import views






urlpatterns =[
    path('form/', views.formpage, name='form'),
    path('', views.homepage,name='home'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('details/<int:pk>', views.details, name='details'),
    path('update/<int:pk>', views.update, name='update'),
    path('category', views.category, name='category'),
    path('football', views.football, name='football'),
    path('article/<int:pk>/comment/', views.add_comment, name='add_comment'),

] 