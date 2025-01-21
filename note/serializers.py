from rest_framework import serializers

from .models import Language, Category, Note, Link


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name', 'date']
        

class CategorySerializer(serializers.ModelSerializer):
    language_name = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'language_name', 'description', 'name', 'date']
        
    def get_language_name(self, obj):
        return obj.language.name


class NoteSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    class Meta:
        model = Note
        fields = ['id', 'category_name', 'name', 'text', 'date', 'hashtag']
        
    def get_category_name(self, obj):
        return obj.category.name
        
    def validate_hashtag(self, value):
        if not value[0] == '#':
            raise serializers.ValidationError("Field hashtag must start with '#'")
        return value
        

