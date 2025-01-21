from django.shortcuts import get_object_or_404
from .models import Language


class LanguageMixin:  
    def get_language(self):
        return get_object_or_404(Language, id=self.kwargs.get('language_id'))