from .views import LanguageViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'language', LanguageViewSet, basename='language')
router.register(r'(?P<language_id>\d+)/category', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls))
]