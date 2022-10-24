from django.contrib import admin
from django.urls import path
from recipes_app.main.views import show_home, create_recipe, edit_recipe, delete_recipe, details_recipe

urlpatterns = (
    path('', show_home, name='show home'),

    path('create/', create_recipe, name='create recipe'),
    path('edit/<int:pk>/', edit_recipe, name='edit recipe'),
    path('delete/<int:pk>/', delete_recipe, name='delete recipe'),
    path('details/<int:pk>/', details_recipe, name='details recipe'),

)


''' 
'/' - home page
'/create' - create recipe page
'/edit/:id' - edit recipe page
'/delete/:id' - delete recipe page
'/details/:id' - recipe details page
'''