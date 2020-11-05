from django.urls import path

from app.views.index import index
from app.views.profiles import delete_profile, edit_profile, profile_index, create_profile
from app.views.expenses import create_expense, delete_expense, edit_expense

urlpatterns = [
    # Index
    path('', index, name='index'),
    # Expenses
    path('create/', create_expense, name='create expense'),
    path('edit/<int:pk>/', edit_expense, name='edit expense'),
    path('delete/<int:pk>/', delete_expense, name='delete expense'),
    # Profiles
    path('profile/', profile_index, name='profile index'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
]
