from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response

from rest_framework import status, viewsets
from .models import *
from .serializers import *
from .mixins import LanguageMixin

class LanguageViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
    
    
class CategoryViewSet(LanguageMixin, viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.none()
    
    def get_queryset(self):
        return Category.objects.filter(language=self.get_language())
    
    def perform_create(self, serializer):
        serializer.save(language=self.get_language())
        return Response({"status": "Created"}, status=status.HTTP_200_OK)


