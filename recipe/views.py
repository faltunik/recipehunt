from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import authentication, permissions
from .models import Recipe
from .serializers import RecipeSerializer


class ListRecipe(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        queryset = Recipe.objects.all()
        serializer = RecipeSerializer(queryset, many=True)        
        return Response(serializer.data) # why we cannot return just serializer


@api_view(['GET'])
def about(request):
    queryset = Recipe.objects.all()
    serializer = RecipeSerializer(queryset, many=True)       
    return Response(serializer)