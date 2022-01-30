from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('recipe/', views.ListRecipe.as_view()),
    path('recipe/<int:pk>', views.ListRecipe.as_view()),
    path('about', views.about),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
