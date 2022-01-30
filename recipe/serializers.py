from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models  import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('title', 'description', )