from django.urls import path

from recipes.views.index import index
from recipes.views.recipes import create_recipe, edit_recipe, delete_recipe, show_details

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_recipe, name='create recipe'),
    path('edit/<int:pk>/', edit_recipe, name='edit recipe'),
    path('delete/<int:pk>/', delete_recipe, name='delete recipe'),
    path('details/<int:pk>/', show_details, name='show details')
]