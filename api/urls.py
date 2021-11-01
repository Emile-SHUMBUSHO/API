from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('recipe/', views.getRecipes),
    path('recipe/create/', views.creatRecipe),
    path('recipe/<str:pk>/update/', views.updateRecipe),
    path('recipe/<str:pk>/delete/', views.deleteRecipe),
    path('recipe/<str:pk>/', views.getRecipe),


]