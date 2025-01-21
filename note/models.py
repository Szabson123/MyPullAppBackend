from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    

class Category(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='category')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)


class Note(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    text = models.TextField()
    hashtag = models.CharField(max_length=255)


class Link(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='link')
    link = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        self.link
