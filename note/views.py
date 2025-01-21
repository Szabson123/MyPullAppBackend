from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response

from rest_framework import status, viewsets
from .models import *
from .serializers import *
from .mixins import GettingObjectsMixin

class LanguageViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
    
    
class CategoryViewSet(GettingObjectsMixin, viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.none()
    
    def get_queryset(self):
        return Category.objects.filter(language=self.get_language())
    
    def perform_create(self, serializer):
        serializer.save(language=self.get_language())


class NoteViewSet(GettingObjectsMixin, viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.none()
    
    def get_queryset(self):
        return Note.objects.filter(category=self.get_category())
    
    def perform_create(self, serializer):
        serializer.save(category=self.get_category())


