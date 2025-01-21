from django.shortcuts import get_object_or_404
from .models import Language, Category


class GettingObjectsMixin:  
    
    def get_language(self):
        return get_object_or_404(Language, id=self.kwargs.get('language_id'))
    
    def get_category(self):
        return get_object_or_404(Category, id=self.kwargs.get('category_id'))
    

