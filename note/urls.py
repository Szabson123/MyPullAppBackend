from .views import LanguageViewSet, CategoryViewSet, NoteViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'language', LanguageViewSet, basename='language')
router.register(r'(?P<language_id>\d+)/category', CategoryViewSet, basename='category')
router.register(r'(?P<category_id>\d+)/note', NoteViewSet, basename='note')

urlpatterns = [
    path('', include(router.urls))
]